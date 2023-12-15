import time

def check_engine_status():
    # Placeholder for an API call or similar to check the engine's status
    # Returns True if the engine has ignited, False otherwise
    print("Checking engine status.")
    return False # return false for testing purposes

def trigger_high_speed_camera():
    # Placeholder for an API call or similar to trigger the camera
    print("High-speed camera activated for rocket launch.")

# Initial status of the engine
engine_ignited = False

while not engine_ignited:
    engine_ignited = check_engine_status()
    if not engine_ignited:
        print("Waiting for engine ignition...")
        time.sleep(0.1)  # Wait for 1/10 second before checking again

trigger_high_speed_camera()
