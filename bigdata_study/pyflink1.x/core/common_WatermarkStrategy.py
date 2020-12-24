from typing import Any

from pyflink.common import WatermarkStrategy, Duration
from pyflink.common.typeinfo import Types
from pyflink.common.watermark_strategy import TimestampAssigner
from pyflink.datastream import StreamExecutionEnvironment


class MyTimestampAssigner(TimestampAssigner):
    def extract_timestamp(self, event: Any, record_timestamp: int) -> int:
        # return: The new timestamp.
       return 0

def demo01():
    env = StreamExecutionEnvironment.get_execution_environment()
    ds = env.from_collection(
        collection = [(1, 'Hi', 'Hello'), (2, 'Hello', 'Hi')],
        type_info=Types.ROW( [Types.INT(), Types.STRING(), Types.STRING()])
    )
    # 给Event添加水位
    # 1.内置水位生成策略
    # 1.1 延迟生成水印: 延迟10s
    watermark_strategy = WatermarkStrategy.for_bounded_out_of_orderness(Duration.of_seconds(10))
    # 1.2 单调递增生成水印:这个也就是相当于上述的延迟策略去掉了延迟时间，以event中的时间戳充当了水印。
    watermark_strategy = WatermarkStrategy.for_monotonous_timestamps()
    # 2. event时间的获取
    watermark_strategy = WatermarkStrategy.for_monotonous_timestamps().with_timestamp_assigner(MyTimestampAssigner())
    """
    在某些情况下，由于数据产生的比较少，导致一段时间内没有数据产生，进而就没有水印的生成，导致下游依赖水印的一些操作就会出现问题，比如某一个算子的上游有多个算子，
    这种情况下，水印是取其上游两个算子的较小值，如果上游某一个算子因为缺少数据迟迟没有生成水印，就会出现eventtime倾斜问题，导致下游没法触发计算。

    所以filnk通过WatermarkStrategy.withIdleness()方法允许用户在配置的时间内（即超时时间内）没有记录到达时将一个流标记为空闲。这样就意味着下游的数据不需要等待水印的到来。

    当下次有水印生成并发射到下游的时候，这个数据流重新变成活跃状态。
    """
    watermark_strategy = WatermarkStrategy.for_bounded_out_of_orderness(Duration.of_seconds(10)).with_idleness(Duration.of_seconds(30))
    ds.assign_timestamps_and_watermarks(watermark_strategy)

    ds.print()

# https://ci.apache.org/projects/flink/flink-docs-release-1.12/api/python/pyflink.common.html#pyflink.common.WatermarkStrategy
if __name__ == '__main__':
    demo01()