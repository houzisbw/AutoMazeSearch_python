#encoding=utf-8

#此处从mazeRobot.pyo模块中载入了方向、停止原因的枚举类型，并且载入了基类
from mazeRobot import Direction,StopReason,MazeRobot;

'''
/// 走迷宫机器人的机器抽象原型类
/// </summary>
/// 
/// <remarks>
/// 【接口扩展说明】
/// 1、run方法可以被调用，通过传入运动方向参数以及预设的运动距离来让机器人在迷宫中往指定方向前进探索；
///    探索的结果可能有以下情况，包括：
///     2.1、顺利向指定方向前进了指定的距离，中途无碰壁；
///     2.2、向指定方向前进的过程中碰壁，机器人将在墙壁的前一个格子位置自动停下来；
///     2.3、在向指定方向前进指定距离的过程中，发现了宝物投放点，机器人将在投放点停下来；
///    以上的三种情况均会在run方法自动回调【doAfterStop】函数，填充到此回调方法的逻辑将在run执行完毕后被自动触发执行，无需额外调用；
///    使用此回调方法可以从参数中获取机器人在最近一次run方法调用中，移动的实际方向与距离，以及停下来的原因；
/// 3、autoRun方法未实现，继承父类的MyMazeRobot类需要实现这个方法，让机器人获得探索寻宝的智能。   
/// ---**---**---**---**---**---**---**---**---**---**---**---**---**---**---**---**---**---**---**---
/// 【你的任务】：
/// 你的任务就是要在这个机器人原型的基础上（即：继承mazeRobot类），
/// 利用run方法操控机器人，以及利用doAfterStop委托事件感知未知地形，
/// 填充在迷宫地图中自动寻宝的外挂逻辑（即：override autoRun方法）
/// 让你的autoRun方法在机器人初始化后，一旦被执行，就能够尽量快地在未知的迷宫地图中探索到宝物投放点；
/// 
/// 注意：
/// 后台自动判题程序会自动载入不同复杂度的迷宫地图并执行autoRun以验证autoRun的AI是否满足效率和正确性的要求；
/// 迷宫地图均为平面地图，路点规模在700*700范围内；请注意优化代码的执行效率！
'''   
class MyMazeRobot(MazeRobot):
    '''要实现迷宫探索的机器人子类'''
    

    def autoRun(self):
        '''
        请重写自动跑迷宫的逻辑：
                1、规划好机器人的探索策略；
                2、规划好机器人自动停机的处理逻辑；
        最终能让机器人对象一旦调用autoRun就能自动在迷宫中找到目标位置
        :return: 无
        '''
        raise NotImplementedError("autoRun:Not Implemented")


    def doAfterStop(self,runDirection,runDistance,stopReason):
        '''
        执行run函数之后自动触发的逻辑
        :param runDirection: 停之前的前进方向
        :param runDistance: 停之前一共走了多少距离
        :param stopReason: 停止的原因
        :return:
        '''
        raise NotImplementedError("doAfterStop:Not Implemented")


##以下代码供调试用，sampleTestCase预留了个简单的用例，
##真实用例会更有挑战性，所以请务必先跑通了sampleTestCase并充分测试才提交
if __name__=="__main__":
    dabai=MyMazeRobot()
    result=dabai.sampleTestCase()
    print("result=[%s]"%result)