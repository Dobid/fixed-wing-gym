from pyfly.pid_controller import PIDController
from gym_fixed_wing.fixed_wing import FixedWingAircraft

env = FixedWingAircraft("../fixed_wing_config.json", config_kw={"steps_max": 1000,
                                                                "observation": {"noise": {"mean": 0, "var": 0}},
                                                                "action": {"scale_space": False}})
env.seed(2)
env.set_curriculum_level(1)
obs = env.reset()

pid = PIDController(env.simulator.dt)
done = False

while not done:
    pid.set_reference(env.target["roll"], env.target["pitch"], env.target["Va"])
    phi = env.simulator.state["roll"].value
    theta = env.simulator.state["pitch"].value
    Va = env.simulator.state["Va"].value
    omega = env.simulator.get_states_vector(["omega_p", "omega_q", "omega_r"])

    action = pid.get_action(phi, theta, Va, omega)
    obs, rew, done, info = env.step(action)

env.render(mode="plot", show=True, block=True)
env.render(mode="plot", show=True, block=True)
print("yeah")

