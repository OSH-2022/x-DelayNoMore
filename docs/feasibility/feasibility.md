# 可行性报告  

## 目录  

[TOC]  

## 理论依据  

### 分布式系统  

**什么是分布式系统？**  

- 分布式系统是一种计算环境，计算所需的组件，算力和资源分布在各个计算设备上。  
- 这些计算设备在物理上是分开的，在硬件上可能是异构，但是它们通过网络相连，对于用户而言是一个整体。  

**为什么需要分布式系统？**  

- 分布式系统和集中式系统是相对的。  
- 随着时代的发展和计算机应用场景的不断扩大，服务器面对的计算任务迅速增大，对算力的需求不断提高，一台单独的服务器难以满足对于计算的需求。  

**分布式系统应用举例**  

寻找梅森素数：  

- 因特网梅森素数大搜索（GIMPS），是一个由志愿者团队协作的项目，从因特网免费下载开放源代码的Prime95和MPrime软件来搜索梅森素数。  
- 利用全球的志愿者闲置的计算资源解决数学难题。  
- https://www.mersenne.org/primes/?press=M82589933  

生物病例研究：  

- Folding@Home  
- 研究蛋白质折叠，误解，聚合及由此引发的生理疾病。  

各种技术的实现：  

- 数字货币技术  
- 区块链技术  
- 游戏的渲染  
- AI 平台  

**分布式系统的优点**  

1. 增强算力  

- 分布式系统可以增强算力，以解决一台机器无法解决的大计算量问题。  
- 突破了计算机可扩展性的瓶颈。以往的集中式计算体系通过增加 CPU 和内存来增强计算机的算力，称为”垂直扩展(scale up)”。  
- 分布式系统通过增加计算设备的数目增强算力，称为”水平扩展(scale out）“。  

2. 增强可用性和稳定性  

- 一台设备的问题：停电，设备故障等意外情况；设备定时的维护需要停机。可用性不高。  
- 当系统中的独立计算设备较多时，分布式系统少数设备的停用对整体性能的影响微乎其微，可用性可以接近100%。  

3. 减少传输延迟  

- 分布式系统的计算设备可以分布在全球的各个位置。用户可以选择这些设备中离自己的手机，PC等个人设备中最近的一台获取信息。  

### ROS 2

**为什么需要 ROS 2？**  

建造一个机器人是一项困难的工作。一个机器人由各个部件组成，例如，驱动器，传感器，控制系统，软件等。要想机器人正常地工作，各个部件的操作必须无缝衔接。有时，一项任务需要多个机器人合作完成，这些机器人之间如何协调工作也是开发者们需要面对的问题。因此必须解决各个进程间的分布式通信的问题。为了应对这些挑战，Robot Operating System，或ROS，应运而生。  

**什么是 ROS 2**  

ROS是用于编写机器人软件程序的一种具有高度灵活性的软件架构。它包含了大量工具软件、库代码和约定协议，旨在简化跨机器人平台创建复杂、鲁棒的机器人行为这一过程的难度与复杂度。$ROS = Plumbing + Tools + Capabilities + Ecosystem$，即：ROS是通讯机制、工具软件包、机器人高层技能以及机器人生态系统的集合体。  

ROS 的主要目标是为机器人研发提供代码复用的支持。ROS是一个分布式的进程（也就是“节点”）框架，这些进程被封装在易于被分享和发布的程序包和功能包中。ROS也支持一种类似于代码储存库的联合系统，这个系统也可以实现工程的协作及发布。这个设计可以使一个工程的开发和实现从文件系统到用户接口完全独立决策（不受ROS限制）。同时，所有的工程都可以被ROS的基础工具整合在一起。  

ROS的几个重要特性：元操作系统、分布式通信机制、松耦合软件框架、丰富的开源功能库。  

**特色**  

亚操作系统：  

不是一个真正意义上的完整的操作系统，而是运行在 Ubuntu Linux 等操作系统上。其底层的任务调度，编译，硬件驱动是由 Linux 完成的，而 ROS 本身可以进行函数调用，硬件抽象等操作系统功能。  

分布式系统：  

将机器人软件的各个功能抽象成节点，节点之间可以相互发送信息。ROS 的开发者可以轻松地构建不同的组件，并通过话题和 messages 将不同的组件连接起来。  

便于测试：  

ROS 组件的 messages 可以发送到多种可视化和远程控制工具上。ROS 的开发者可以使用模拟的机器人，而不是真实的硬件，来实现更加高效简易的测试。  

强大的软件包：  

ROS 的总体架构可以看成两层。底层是上面介绍的元操作系统，而高层则是用户提供的软件包，可以实现定位绘图，行动规划，感知，模拟等功能。  

**ROS1 vs ROS2**  

（1）ROS1主要构建于Linux系统之上，而ROS2支持构建的系统包括Linux、windows、Mac、RTOS，甚至没有操作系统的裸机。  

（2）ROS1的通讯系统基于TCPROS/UDPROS，强依赖于master节点的处理， 一旦master异常，将导致全系统通信故障。ROS2的通讯系统是基于DDS（一种分布式实时系统中数据发布/订阅的标准解决方案），同时在ROS2内部提供了DDS的抽象层实现，用户不需要关注底层DDS的提供厂家。  

（3）ROS中最重要的一个概念就是“节点”，基于发布/订阅模型的节点使用，可以让开发者并行开发低耦合的功能模块，并且便于进行二次复用。得益于DDS的加入，ROS2的发布/订阅模型也会发生改变。  

（4）ROS1的架构中Nodelet和TCPROS/UDPROS是并列的层次，都是负责通讯的，实际上Nodelet是为同一个进程中的多个节点提供一种更优化的数据传输方式。ROS2中也保留了这种数据传输方式，叫“Intra-process”，同样也是独立于DDS。  

**ROS 2 源代码分析**  

Topic模块：  

Topic进行的是异步通信，采用发布/订阅模型，一个或多个节点（发布者）可以在某个Topic中发布消息，另外的一个或多个节点（订阅者）从Topic中接收消息。例如：在执行命令$ros2$ $topic$ $list$ $<command>$时，将依次运行：  

```python
from ros2cli.command import add_subparsers_on_demand
from ros2cli.command import CommandExtension


class TopicCommand(CommandExtension):
    """Various topic related sub-commands."""

    def add_arguments(self, parser, cli_name):
        self._subparser = parser
        parser.add_argument(
            '--include-hidden-topics', action='store_true',
            help='Consider hidden topics as well')

        # add arguments and sub-commands of verbs
        add_subparsers_on_demand(
            parser, cli_name, '_verb', 'ros2topic.verb', required=False)

    def main(self, *, parser, args):
        if not hasattr(args, '_verb'):
            # in case no verb was passed
            self._subparser.print_help()
            return 0

        extension = getattr(args, '_verb')

        # call the verb's main method
        return extension.main(args=args)
```

```python
from ros2cli.node.strategy import add_arguments as add_strategy_node_arguments
from ros2cli.node.strategy import NodeStrategy
from ros2topic.api import get_topic_names_and_types
from ros2topic.verb import VerbExtension


class ListVerb(VerbExtension):
    """Output a list of available topics."""

    def add_arguments(self, parser, cli_name):
        add_strategy_node_arguments(parser)

        parser.add_argument(
            '-t', '--show-types', action='store_true',
            help='Additionally show the topic type')
        parser.add_argument(
            '-c', '--count-topics', action='store_true',
            help='Only display the number of topics discovered')
        # duplicate the following argument from the command for visibility
        parser.add_argument(
            '--include-hidden-topics', action='store_true',
            help='Consider hidden topics as well')
        parser.add_argument(
            '-v', '--verbose', action='store_true',
            help='List full details about each topic')

    @staticmethod
    def show_topic_info(topic_info, is_publisher):
        message = ('Published' if is_publisher else 'Subscribed') + ' topics:\n'
        for (topic_name, topic_types, pub_count, sub_count) in topic_info:
            count = pub_count if is_publisher else sub_count
            if count:
                topic_types_formatted = ', '.join(topic_types)
                count_str = str(count) + ' ' + ('publisher' if is_publisher else 'subscriber') \
                    + ('s' if count > 1 else '')
                message += f' * {topic_name} [{topic_types_formatted}] {count_str}\n'
        return message

    def main(self, *, args):
        topic_info = []
        with NodeStrategy(args) as node:
            topic_names_and_types = get_topic_names_and_types(
                node=node,
                include_hidden_topics=args.include_hidden_topics)
            for (topic_name, topic_types) in topic_names_and_types:
                if args.verbose:
                    pub_count = node.count_publishers(topic_name)
                    sub_count = node.count_subscribers(topic_name)
                    topic_info.append((topic_name, topic_types, pub_count, sub_count))
                else:
                    topic_info.append((topic_name, topic_types, 0, 0))

        if args.count_topics:
            print(len(topic_names_and_types))
        elif topic_names_and_types:
            if args.verbose:
                print(self.show_topic_info(topic_info, is_publisher=True))
                print(self.show_topic_info(topic_info, is_publisher=False))
            else:
                for (topic_name, topic_types, _, _) in topic_info:
                    msg = '{topic_name}'
                    topic_types_formatted = ', '.join(topic_types)
                    if args.show_types:
                        msg += ' [{topic_types_formatted}]'
                    print(msg.format_map(locals()))
```

### DDS  

- DDS(Data Distribution Service)，数据分发服务。  
- 实时系统的DDS是一个对象管理组织(Object Management Group)发布的的机器对机器(machine-to-machine)标准，旨在实现基于发布-订阅模式的可靠的，高性能的，可相互操作的，实时的数据交换。  

一个参与者(participant)代表了一个用户，每个DDS用户都必须通过Participant对全局数据空间进行读写。  

- 发布者(Publisher)是数据的发布者，可以和一个或多个 Data Writer 相连，发布一种或多种话题(topic)的信息。  
- 订阅者(Subscriber)是数据读入的执行者，一个订阅者可以和多个 Data Reader 相连，进行一个或多个话题的消息。  
- 数据写入器(Data Writer)，应用向发布者写入数据的对象，一个数据写入器和一种topic对应.  
- 数据读取器(Data Reader)，应用从订阅者获取数据的对象，一个数据读取器和一个topic对应。  

QoS Policy: Quality of Service Policy. 服务质量原则。主要从时间限制、可靠性、持续性、历史记录几个方面，控制了各方面与底层的通讯机制，满足用户针对不同场景的数据应用需求。其具体控制有以下几个方面：  

- Deadline  
- History  
- Reliability  
- Durability  

## 技术依据  

### Ray

#### Ray 简介  

Ray 是一种通用的集群计算框架，既支持模型的训练，又支持对环境的仿真或与环境的交互，还支持模型服务。Ray所面临的任务涵盖了从轻量级、无状态的计算任务（例如仿真）到长时间运行的、有状态的计算任务（例如训练）。为了满足这些任务的需求，Ray 实现了一套统一的接口，这套接口既能表达**基于任务的并行计算**(task-parallel)，又能表达**基于行动器的并行计算**(actor-based)。为了满足性能需求，Ray 使用了分布式的任务调度器和元数据存储器设计，从而满足了 Ray 的毫秒百万级并发量的需求。Ray 还为任务和行动器提供了基于 Lineage 的容错机制，同时为元数据存储提供了基于复制的容错机制。  

Ray 设计并实现了首个将训练、仿真和服务统一起来的分布式计算框架，基于动态任务执行引擎统一了有状态并行（**行动器**）和无状态并行（**任务**），并保障了框架的高可扩展性和高容错性。  

#### Ray 架构  

Ray 的架构由应用层和系统层组成，其中应用层实现了 Ray 的 API，作为前端供用户使用，而系统层则作为后端来保障Ray的高可扩展性和容错性。整体的架构图如下图所示：  

![](https://pic1.zhimg.com/80/v2-063d38543cd63364eec5994946620b38_720w.jpg)

<center>Ray的架构图</center>

##### 应用层  

应用层中有三种类型的进程：  

- **驱动器进程** (Driver Process): 执行用户程序的进程。顾名思义，所有操作都需要由主进程来驱动。  
- **工作器进程** (Worker Process): 执行由驱动器或其他工作器调用的任务（远程函数）的无状态的进程。工作器由系统层分配任务并自动启动。当声明一个远程函数时，该函数将被自动发送到所有的工作器中。在同一个工作器中，任务是串行地执行的，工作器并不维护其任务与任务之间的局部状态，即在工作器中，一个远程函数执行完后，其局部作用域的所有变量将不再能被其他任务所访问。  
- **行动器进程** (Actor Process): 行动器被调用时只执行其所暴露的方法。行动器由工作器或驱动器显式地进行实例化。与工作器相同的是，行动器也会串行地执行任务，不同的是行动器上执行的每个方法都依赖于其前面所执行的方法所导致的状态。  

三种进程体现到Python代码中如下：  

```python
@ray.remote
def f(x):
    # ==== 工作器进程 ====
    return x * x

@ray.remote
class Counter(object):
    def __init__(self):
        # ==== 行动器进程 ====
        self.value = 0

    def increment(self):
        # ==== 行动器进程 ====
        self.value += 1
        return self.value

if __name__ == "__main__":
    # ==== 驱动器进程 ====
    object_ref = f.remote(2)
    assert ray.get(object_ref) == 4

    counter = Counter.remote()
    refs = []
    for i in range(10):
        ref = counter.increment.remote()
        refs.append(ref)
    for i, ref in enumerate(refs):
        assert ray.get(ref) == i + 1
```

##### 系统层  

系统层由三个主要部件组成：全局控制存储器 (**G**lobal **C**ontrol **S**tore)、分布式调度器 (Distributed Scheduler)和分布式对象存储器 (Distributed Object Store)。这些部件在横向上是可扩展的，即可以增减这些部件的数量，同时还具有一定的容错性。  

**GCS**  

GCS设计的初衷是让系统中的各个组件都变得尽可能地无状态，因此GCS维护了一些全局状态：  

- 对象表 (Object Table)：记录每个对象存在于哪些节点  
- 任务表 (Task Table)：记录每个任务运行于哪个节点  
- 函数表 (Function Table)：记录用户进程中定义的远程函数  
- 事件日志 (Event Logs)：记录任务运行日志  

**分布式调度器**  

Ray中的任务调度器被分为两层，由一个全局调度器和每个节点各自的局部调度器组成。为了避免全局调度器负载过重，**在节点创建的任务首先被提交到局部调度器，如果该节点没有过载且节点资源能够满足任务的需求（如GPU的需求），则任务将在本地被调度，否则任务才会被传递到全局调度器**，考虑将任务调度到远端。由于Ray首先考虑在本地调度，本地不满足要求才考虑在远端调用，因此这样的调度方式也被称为自底向上的调度。  

下图展示了Ray的调度过程，箭头的粗细表示过程发生频率的高低。用户进程和工作器向本地调度器提交任务，大多数情况下，任务将在本地被调度。少数情况下，局部调度器会向全局调度器提交任务，并向GCS传递任务的相关信息，将任务涉及的对象和函数存入全局的对象表和函数表中，然后全局调度器会从GCS中读取到信息，并选择在其他合适的节点上调度这一任务。更具体地来说，全局调度器会根据任务的请求选出具有足够资源的一系列节点，并在这些节点中选出等待时间最短的一个节点。  

![](https://pic1.zhimg.com/80/v2-b047e880cf58ec9c6670778b84fd5910_720w.jpg)

**分布式对象存储器**  

Ray实现了一个内存式的分布式存储系统来存储每个任务的输入和输出。Ray通过内存共享机制在每个节点上实现了一个对象存储器 (Object Store)，从而使在同一个节点运行的任务之间不需要拷贝就可以共享数据。当一个任务的输入不在本地时，则会在执行之前将它的输入复制到本地的对象存储器中。同样地，任务总会将输出写入到本地的对象存储器中。这样的复制机制可以减少任务的执行时间，因为**任务永远只会从本地对象存储器中读取数据（否则任务不会被调度）**，并且消除了热数据可能带来的潜在的瓶颈。  

#### Ray 编程

Ray中有两个重要的概念：**任务**(Task)和**行动器**(Actor)。**Ray编程模型**是指Ray框架基于任务和行动器这两个重要需求所向用户提供的一套API及其编程范式。下表展示了Ray提供的核心API。  

| 代码                                                         | 说明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| futures = f.remote(args)                                     | 远程地执行函数f。f.remote()以普通对象或future对象作为输入，返回一个或多个future对象，非阻塞执行。 |
| objects = ray.get(futures)                                   | 返回与一个或多个future对象相关联的真实值，阻塞执行           |
| ready_futures = ray.wait(futures, k, timeout)                | 当futures中有k个future完成时，或执行时间超过timeout时，返回futures中已经执行完的future |
| actor = Class.remote(args) futures = actor.method.remote(args) | 将一个类实例化为一个远程的行动器，并返回它的一个句柄。然后调用这个行动器的method方法，并返回一个或多个future. 两个过程均为非阻塞的。 |

任务是指在无状态的工作器中执行的远程函数。远程函数被调用时会立即返回一个future对象，而真正的返回值可以通过ray.get(<future对象>)的方式来获取。**这样的编程模型既允许用户编写并行计算代码，同时又提醒用户要关注数据之间的依赖性。**  

**任务的编程范式**如下：  

1. 注册任务：在需要注册为任务的函数上加上@ray.remote装饰器  
2. 提交任务：在调用具有@ray.remote装饰器的函数时，需要带上.remote()而不是直接调用  
3. 非阻塞提交：无论任务的运行需要多少时间，在提交任务后都会立即返回一个ObjectRef对象  
4. 按需阻塞获取结果：在你需要函数的返回值时，可以通过ray.get来获取  

**行动器的编程范式**如下：  

1. 注册行动器：在需要注册为行动器的类上加上@ray.remote装饰器  
2. 实例化行动器：相比于普通Python类的实例化，需要在类名后加上.remote  
3. 提交方法调用：调用行动器的方法时，同样需要带上.remote()而不是直接调用  
4. 非阻塞提交：无论方法的运行需要多少时间，在提交任务后都会立即返回一个ObjectRef对象（同一行动器实例下，方法会按照提交顺序串行地运行）  
5. 按需阻塞获取结果：在需要方法运行的返回值时，可以通过ray.get来获取  

#### Ray 应用  

在本项目中，使用Ray将多个节点的算力结合起来。将部署的ROS节点（分布式计算集群节点）发出的任务通过Ray中的分布式计算框架进行计算调度后返回到各个节点中去。  

## 技术路线

Step 1：ROS 多节点部署  

利用 ROS 部署多个节点，每个节点完成某一项任务，各个节点之间可以相互通信，实现各个节点之间相互配合完成一项任务。主要为基于 ROS 2 的计算模型搭建。  

Step 2：使用 Ray 搭建分布式集群  

1. 在 ROS 基础平台建立分布式集群，将整个分布式系统作为一个算力平台；  
2. ROS 的每个节点作为分布式计算集群的一个节点，即每个节点兼顾了 ROS 的节点和分布式集群的节点，ROS 的任务是在两个集群之间进行传递；  
3. （模式）在和 ROS 相同的节点上部署分布式集群，某个节点发布的算力请求，其他节点可以通过分布式框架为其提供支持。  

Step 3：实现 ROS 和 Ray 分布式集群的耦合  

每个节点既是 ROS 的节点，又是 Ray 分布式集群的节点，两个集群直到彼此的存在。  
ROS 的 DDS 通信模式和 Ray 是松耦合的，为这一步的实现提供了可行性和便捷性。  
实现的功能为：各个 ROS 节点发送算力的信息，Ray 作为一个分布式计算框架对信息进行处理，计算结束之后将结果返回给 ROS。  

Step 4：适配深度学习模型  

- 利用 Ray 通过深度学习实现任务的分配和部署。  
- 实现任务和信息在ROS，Ray 和深度学习框架之间的高效传递，整合和返回。
