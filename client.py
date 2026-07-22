class VoiceFirstLogisticsCoordinatorClient:
    def coordinate(self, voice_transcript: str, shipment_id: str) -> dict:
        txt = voice_transcript.lower()
        if "reschedule" in txt or "delay" in txt:
            action = "UPDATE_DISPATCH_TIME"
            status = "RESCHEDULED_TO_NEXT_WINDOW"
        elif "status" in txt or "where" in txt:
            action = "FETCH_REALTIME_GPS"
            status = "LOCATION_IN_TRANSIT"
        else:
            action = "CONFIRM_RECEIPT"
            status = "DELIVERY_CONFIRMED"
        return {
            "coordination_status": status,
            "action_dispatched": f"{action} for shipment {shipment_id}"
        }
