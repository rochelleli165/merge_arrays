import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32MultiArray


class FirstArrayPublisher(Node):

    def __init__(self):
        super().__init__('first_array_publisher')
        self.publisher_ = self.create_publisher(Int32MultiArray, '/input/array1', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Int32MultiArray()
        msg.data = [1, 4, 8, 12, 26]
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    first_array_publisher = FirstArrayPublisher()

    rclpy.spin(first_array_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    first_array_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
