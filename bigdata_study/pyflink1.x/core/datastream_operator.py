from pyflink.common.typeinfo import Types
from pyflink.datastream import StreamExecutionEnvironment, CoMapFunction


class MyCoMapFunction(CoMapFunction):

    def map1(self, value):
        return value[0] #str(value[0] + 1)

    def map2(self, value):
        return value[0]

def operators():
    s_env = StreamExecutionEnvironment.get_execution_environment()
    s_env.set_parallelism(1)
    s_env.set_python_executable(r"D:/ProgramData/Anaconda3/envs/penter/python.exe")
    ds1 = s_env.from_collection([(1, 'Hi', 'Hello'), (2, 'Hello', 'Hi')],
                             type_info=Types.ROW(
                                 [Types.INT(), Types.STRING(), Types.STRING()])
                             )
    ds2 = s_env.from_collection([(3, 'Hi2', 'Hello2'), (4, 'Hello2', 'Hi2')],
                             type_info=Types.ROW(
                                 [Types.INT(), Types.STRING(), Types.STRING()])
                             )

    # Connect DataStream,DataStream → ConnectedStreams
    cs = ds1.connect(ds2).map(MyCoMapFunction())

    cs.print()
    s_env.execute('operators')

# https://ci.apache.org/projects/flink/flink-docs-release-1.12/dev/stream/operators/
if __name__ == '__main__':
    operators()