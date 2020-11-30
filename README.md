# ros_control

# What is Control in Robotics

Imagine you have to eat by taking food from your plate on the desk and putting it in your mouth with fork/spoon. You would of course have to pick the food up and move your hands in the direction of your mouth and stop the movement of the arm when the spoon is in your mouth. You would also want to ensure that the movement is in such a way that it is not too fast such that  the spoon injures you, or too slow that you have to wait forever. In fact, you also want to ensure that the movement of your arm stops when it reaches the destination ( the mouth) and that you do not take the food into your nose instead. This process needs us to accurately and precisely control the position and speed of our hands throughout the motion. 

In the same way, if we have a robotic arm or manipulutor and we want it to perfrom a desired task such as pick and place, the movement of the end effector must be such that it does not hit the table hard and must also place the object at desired location in the shortest possible time. This process needs us to track and control the position and velocity of the robot joint throughout the course of motion.

One of the  most popular control strategy to achieve this task is PID. In short, the PID quickly drives the system to its desired set point and reduces its speed as it aprroaches the goal. This course is not about control engineering. Thus, we would not go into details of the PID and how it works.

# What is ros_control

ROS basically provides us with packages and interfaces that allow us to control the motion of our robots using PID controllers. The original idea behind ros_control is from pr2 controlller_manager used to control the PR2 robot.
The work of [Adolfo Rodrígiez et al](https://github.com/ros-controls/ros_control), the creators and maintainers of the ros_control packages,  allow us to use ros_control package with any robot with the set of interfaces it provides. We do not need to bother about issues like sampling rate, derivative kick, etc. All these are handled by our controller. We however would need it if we want to write our own controller package. ros_control simply saves is time of rewriting controllers code everytime we need to control our robot.


In a real robot, what we are controlling is the position ans speed of the eahc motors at each joint.

A ros controller basically would receive a set point or desired position ans use its feedback mechanism to control the output using the current state of the actuators at each timestep. Thus, our ros ros controller typically uses a PID controller to achieve desired set points.

To perform a desired motion by moving each joint,  we make use of ROS controller in each joint. This ros controller must be compatible  with the hardware interface mentioned inside
the transmission tags.

ROS controllers do not interact directly with the hardware. Rather, there is an hardware interface which they comunicate with. This hardware interface is the middleman or the mediator between the ROS controllers and the real hardware or simulator.
There are different types of ros controllers like the position controllers, velocity controllers, effort
controllers, and so on. ros_control provides this controllers for us to use depending on the hardware interface we specify for each joint or that we are working with.

# Types of ROS Controllers
There are different types of controllers that allow us to interact in different ways with joints.
The one we would use is dependent on the kind of commands the joint accepts.
The controller type is basically telling us how to achieve a goal which is our input command

1. **joint_state_controller**: This controller reads joint positions and publish them on to the topic "/joint_states". This controller does not send any command to the actuators.It is like a sensor for our joints.

2. **effort_controller**: It allows us to send command to an effort interface. That is the joint we want to control accept effort commands (current and velocity) directly. The following are types of effort controllers.

    * **joint_position_controller**: This controller plugin allow us to send position value (radians or meters) as input. The error between desired and current position is mappeed as output effort through the PID loop

    * **joint_velocity_controller**: This controller plugin allow us to send velocity value (radians/sec or meter/sec) as input.  The error between desired and current velocity is mappeed as output effort through the PID loop

    * **joint_effort_controller**: This controller plugin allow us to forces or torques directly as input to actuators. The PID gain values have no effect on output effort.

3.  **position_controllers**: It allows us to send command to a position interface. That is the joint actuator we want to control accept position commands directly. 
    * **joint_position_controller**: The velocity_controllers plugin accepts only velocity values as input.

4.  **velocity_controllers**: It allows us to send command to a velocity interface. That is the joint actuator  we want to control accept velocity commands directly. 
    * **joint_velocity_controller**: The velocity_controllers plugin accepts only velocity values as input.




![alt text](https://github.com/jimohafeezco/manipulator/blob/master/media/contol_one_joint.gif)

![alt text](https://github.com/jimohafeezco/manipulator/blob/master/media/third.gif)

![alt text](https://github.com/jimohafeezco/manipulator/blob/master/media/kuka.gif)
