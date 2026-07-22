from client import VoiceFirstLogisticsCoordinatorClient

def main():
    client = VoiceFirstLogisticsCoordinatorClient()
    res = client.coordinate(voice_transcript="Can you check where driver for shipment SHP-9021 is right now?", shipment_id="SHP-9021")
    print(f"Status: {res['coordination_status']}")
    print(f"Action: {res['action_dispatched']}")

if __name__ == "__main__":
    main()
