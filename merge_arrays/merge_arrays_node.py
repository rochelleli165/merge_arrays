import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32MultiArray


class MergeArraysNode(Node):
    array1 = [0]
    array2 = [0]
    new_array = []
    def __init__(self):
        super().__init__('merge_arrays_node')
        self.publisher_ = self.create_publisher(Int32MultiArray, '/output/array',10)
        # Creates subscribers
        self.subscription = self.create_subscription(Int32MultiArray,'/input/array1',self.listener_callback,10)
        self.subscription = self.create_subscription(Int32MultiArray,'/input/array2',self.second_listener_callback,10)

        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Int32MultiArray()

        if len(self.new_array) == 0:
            exit()

        msg.data = self.new_array

        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: %s' % msg.data)
        self.i += 1



    def listener_callback(self, msg):
        self.array1 = msg.data

    def second_listener_callback(self, msg):
        self.array2 = msg.data
        self.new_array = merge(self.array1, self.array2)

def merge(arr1, arr2):
        arr3 = (arr1+arr2)
        return sorted(arr3)

def main(args=None):
    rclpy.init(args=args)

    merge_arrays_node = MergeArraysNode()

    rclpy.spin(merge_arrays_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    merge_arrays_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

