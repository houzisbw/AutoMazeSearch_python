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

    def __init__(self):
        self.x=700              #机器人自己的坐标,放在1400*1400的地图中间
        self.y=700

        self.map = []           #宝物地图，一个二维的list,大小为1500*1500
        self.roadStack=[]       #dfs时用来记录走过路程的栈，栈里的元素是(x,y)的元组，表示地图方格的坐标

        self.initMap()          #初始化地图为0，0表示未走过的路

        self.runDist = 0        #获得doAfter函数走过的距离
        self.hasFound = False   #找到宝物与否的bool,一旦找到宝物就退出while循环结束程序

    #初始化地图，0表示没有走过的点
    def initMap(self):
        self.map = [([0]*1400) for i in range(0,1400)]

    def autoRun(self):
        '''
        请重写自动跑迷宫的逻辑：
                1、规划好机器人的探索策略；
                2、规划好机器人自动停机的处理逻辑；
        最终能让机器人对象一旦调用autoRun就能自动在迷宫中找到目标位置
        :return: 无
        '''


        #将机器人当前位置入栈
        originPos = (self.x,self.y)
        self.roadStack.append(originPos)
        self.map[self.y][self.x]=1 ###不能少,初始点走过了

        #while循环，当栈空时退出
        while ((not len(self.roadStack)==0) and self.hasFound == False) :              ###########################


            #更新机器人当前位置为栈顶元素
            self.x = self.roadStack[-1][0]
            self.y = self.roadStack[-1][1]

            #print 'x,y',self.y,self.x

            #机器人向4个方向探测，每次走一步
            #向右边探测
            if(not self.map[self.y][self.x + 1]):
                self.run(Direction.right, 1)
                if self.runDist > 0:               #如果走过的距离大于0，则入栈新到达的位置
                    self.roadStack.append((self.x,self.y))
            #向左边探测
            elif(not self.map[self.y][self.x - 1]):
                self.run(Direction.left, 1)
                if self.runDist > 0:               #如果走过的距离大于0，则入栈新到达的位置
                    self.roadStack.append((self.x,self.y))
            #向下边探测
            elif(not self.map[self.y+1][self.x]):
                self.run(Direction.down, 1)
                if self.runDist > 0:               #如果走过的距离大于0，则入栈新到达的位置
                    self.roadStack.append((self.x,self.y))
            #向上边探测
            elif(not self.map[self.y-1][self.x]):
                self.run(Direction.up, 1)
                if self.runDist > 0:               #如果走过的距离大于0，则入栈新到达的位置
                    self.roadStack.append((self.x,self.y))


            else:  #4个方向走不通说明该回退一步了
                if len(self.roadStack)==0:
                    break
                else:
                    #temp = self.roadStack.pop()  #出栈，得到路点
                    self.roadStack.pop()
                    temp = self.roadStack[-1]

                    directionX = temp[0]-self.x  #得到来时的方向
                    directionY = temp[1]-self.y

                    #计算回退的方向
                    returnDir = self.caculateReturnDirection(directionX,directionY)

                    #回退一步
                    self.run(returnDir,1)


    def caculateReturnDirection(self,dx,dy):  #计算回退的方向
        returnDirection = 0
        if dx == 1 and dy == 0:
            returnDirection = Direction.right
        elif dx == -1 and dy == 0:
            returnDirection = Direction.left
        elif dx == 0 and dy == 1:
            returnDirection = Direction.down
        else:
            returnDirection = Direction.up
        return returnDirection

    def markRoadAccordingToDirection(self,runDirection):   #根据方向来标记走到的路点以及更新自己的位置
        if runDirection == Direction.right:
            self.x +=1
        elif runDirection == Direction.left:
            self.x -=1
        elif runDirection == Direction.up:
            self.y -=1
        else:
            self.y +=1

    def doAfterStop(self,runDirection,runDistance,stopReason):
        '''
        执行run函数之后自动触发的逻辑
        :param runDirection: 停之前的前进方向
        :param runDistance: 停之前一共走了多少距离
        :param stopReason: 停止的原因
        :return:
        '''
        #获得走过的距离
        self.runDist = runDistance


        if stopReason == StopReason.arrive:
            #标记走到的路点
            self.markRoadAccordingToDirection(runDirection)
            #更新地图：该点已经走过了
            self.map[self.y][self.x]=1


        elif stopReason == StopReason.hitWall:

            #标记地图该点(墙)不可走
            if runDirection == Direction.up:
                self.map[self.y-1][self.x]=1
            elif runDirection == Direction.down:
                self.map[self.y+1][self.x]=1
            elif runDirection == Direction.left:
                self.map[self.y][self.x-1]=1
            else:
                self.map[self.y][self.x+1]=1

        else:
            #找到宝物,退出while
            self.hasFound = True





##以下代码供调试用，sampleTestCase预留了个简单的用例，
##真实用例会更有挑战性，所以请务必先跑通了sampleTestCase并充分测试才提交
#import time
if __name__=="__main__":
    #t = time.time()
    dabai=MyMazeRobot()
    result=dabai.sampleTestCase()
    #print time.time()-t
    print("result=[%s]"%result)