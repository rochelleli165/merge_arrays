import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32MultiArray


class SecondArrayPublisher(Node):

    def __init__(self):
        super().__init__('second_array_publisher')
        self.publisher_ = self.create_publisher(Int32MultiArray, '/input/array2', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Int32MultiArray()
        msg.data = [3, 9, 18, 20, 30]
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    second_array_publisher = SecondArrayPublisher()

    rclpy.spin(second_array_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    second_array_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
