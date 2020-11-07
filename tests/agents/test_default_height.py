import holodeck
import uuid
from copy import deepcopy

from tests.utils.equality import almost_equal

uav_config2 = {
    "name": "test_max_height",
    "world": "TestWorld",
    "main_agent": "uav1",
    "agents": [
        {
            "agent_name": "uav1",
            "agent_type": "UavAgent",
            "sensors": [
                {
                    "sensor_type": "LocationSensor",
                }
            ],
            "control_scheme": 0,
            "location": [0, 0, 2],
            # "max_height": 50 - 11.8283691 # in centimeters # If you uncomment this, you'll see that the test fails
        }
    ]
}

def test_default_height():
    """Make sure the location sensor updates after a teleport. Also verifies that the coordinates for the teleport
    command match the coordinates used by the location sensor
    """
    # binary_path = holodeck.packagemanager.get_binary_path_for_package("DefaultWorlds")

    # assert (False), "test3"

    # Spawn the UAV 10 meters up
    # cfg["agents"][0]["location"] = [0, 0, 2]

    with holodeck.environments.HolodeckEnvironment(scenario=uav_config2,
                                                   show_viewport=False,
                                                   start_world=False
                                                   )as env:

        # assert (False), "test"
        command = [0, 0, 0, 1000]
        # assert (False), "agh"
        # state = env.tick()
        # max_height = 5 # in meters
        # max_height = state["max_height"]
        # changing bed space, leaving and come back in jan, or leaving bed space after thanks

        
        moving = True
        for _ in range(10):
            state = env.tick()
            sensed_loc = state["LocationSensor"]
            for i in range(50):
                state, reward, terminal, _ = env.step(command)
            state = env.tick()
            assert ((sensed_loc[2] < state["LocationSensor"][2]) and not (almost_equal(sensed_loc[2], state["LocationSensor"][2]))), "WHY IT STOP"
