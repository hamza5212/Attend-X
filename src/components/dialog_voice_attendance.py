import streamlit as st

from src.pipeline.voice_pipeline import process_bulk_audio

from src.database.config import supabase

import pandas as pd


from src.components.dialog_attendance_result import show_attendance_result
from datetime import datetime

@st.dialog("Voice Attendance")
def voice_attendance_dialog(selected_subject_id):
    st.write(
        "Record audio of students saying 'I am present'. "
        "The system will attempt to recognize enrolled students."
    )

    audio_data = st.audio_input("Record classroom audio")

    if st.button(
        "Analyze Audio",
        width="stretch",
        type="primary",
        disabled=(audio_data is None),
    ):
        # Clear results from a previous recording.
        st.session_state.pop("voice_attendance_results", None)

        with st.spinner("Processing audio data..."):
            try:
                enrolled_res = (
                    supabase.table("subject_students")
                    .select("*, students(*)")
                    .eq("subject_id", selected_subject_id)
                    .execute()
                )
                enrolled_students = enrolled_res.data or []

                if not enrolled_students:
                    st.warning("No students are enrolled in this subject.")
                    return

                candidates_dict = {
                    node["students"]["student_id"]:
                        node["students"]["voice_embedding"]
                    for node in enrolled_students
                    if node.get("students")
                    and node["students"].get("voice_embedding")
                }

                if not candidates_dict:
                    st.error(
                        "No enrolled students have registered voice profiles."
                    )
                    return

                # audio_data is available because the button is disabled
                # until a recording is supplied.
                audio_bytes = audio_data.getvalue()

                detected_scores = process_bulk_audio(
                    audio_bytes, candidates_dict
                )

                results = []
                attendance_to_log = []

                current_timestamp = datetime.now().astimezone().isoformat(
                    timespec="seconds"
                )

                for node in enrolled_students:
                    student = node.get("students")
                    if not student:
                        continue

                    student_id = student["student_id"]
                    score = detected_scores.get(student_id, 0.0)
                    is_present = score > 0

                    results.append({
                        "Name": student["name"],
                        "ID": student_id,
                        "Score": round(float(score), 3),
                        "Status": (
                            "✅ Present" if is_present else "❌ Absent"
                        ),
                    })

                    attendance_to_log.append({
                        "student_id": student_id,
                        "subject_id": selected_subject_id,
                        "timestamp": current_timestamp,
                        "is_present": bool(is_present),
                    })

                st.session_state.voice_attendance_results = (
                    pd.DataFrame(results),
                    attendance_to_log,
                )

            except Exception as e:
                st.error(f"Audio analysis failed: {e}")
                return

    saved_results = st.session_state.get("voice_attendance_results")

    if saved_results:
        st.divider()
        df_results, logs = saved_results
        show_attendance_result(df_results, logs)
