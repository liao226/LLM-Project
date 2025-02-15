/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80030
 Source Host           : localhost:3306
 Source Schema         : database

 Target Server Type    : MySQL
 Target Server Version : 80030
 File Encoding         : 65001

 Date: 31/12/2024 17:17:51
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for calculate_question
-- ----------------------------
DROP TABLE IF EXISTS `calculate_question`;
CREATE TABLE `calculate_question`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `question` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `index` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `generate_time` datetime(6) NULL DEFAULT NULL,
  `solution` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `user_answer` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `flag` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `comment` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 29 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of calculate_question
-- ----------------------------
INSERT INTO `calculate_question` VALUES (1, '在一条长120米的道路上，每隔10米种一棵树，两端都要种树。问一共需要种多少棵树？', 'test', '2', '2024-12-30 21:15:57.180490', '13', '13', 'true', '解析：这是一个典型的植树问题。根据植树问题的公式，总树数 = 间隔数 + 1。首先，我们需要计算出间隔数。间隔数 = 总长度 / 间隔距离 = 120米 / 10米 = 12个间隔。由于两端都要种树，所以总树数 = 12 + 1 = 13棵树。');
INSERT INTO `calculate_question` VALUES (2, '请计算数对(3, 4)和(5, -2)之间的曼哈顿距离。', 'test', '2', '2024-12-30 21:16:09.460774', '8', '8', 'true', '解析：曼哈顿距离是两个点在坐标系中沿坐标轴走的距离之和。对于点A(x1, y1)和点B(x2, y2)，曼哈顿距离的计算公式为|x1 - x2| + |y1 - y2|。因此，对于点(3, 4)和(5, -2)，计算过程如下：|3 - 5| + |4 - (-2)| = | -2 | + |6| = 2 + 6 = 8。');
INSERT INTO `calculate_question` VALUES (3, '3x + 5 = 20', 'test', '2', '2024-12-30 21:16:16.011330', '5', '5', 'true', '解析：这道题目是一个简单的一元一次方程。首先，我们可以通过减去5来消去常数项，得到3x = 15。然后，通过除以3来解x，得到x = 5。');
INSERT INTO `calculate_question` VALUES (4, '3.5 * 4.2 + 1.8 / 0.9 =', 'test', '2', '2024-12-30 21:16:26.436597', '16.7', '16.7', 'true', '解析：首先计算乘法部分，3.5乘以4.2得到14.7。然后计算除法部分，1.8除以0.9得到2。最后将这两个结果相加，14.7加上2得到最终答案。');
INSERT INTO `calculate_question` VALUES (5, '已知数对(3, 5)表示的位置在平面直角坐标系中位于第几象限？', 'test', '2', '2024-12-30 21:16:34.778268', '第一象限', '一', 'true', '解析：在平面直角坐标系中，第一象限的x和y坐标均为正，第二象限的x坐标为负，y坐标为正，第三象限的x和y坐标均为负，第四象限的x坐标为正，y坐标为负。数对(3, 5)中，x=3为正，y=5为正，因此该位置位于第一象限。');
INSERT INTO `calculate_question` VALUES (6, '3.45 * 1.2 + 2.3 =', 'test', '2', '2024-12-30 21:16:41.154455', '6.44', '6.44', 'true', '解析：首先计算小数乘法，3.45乘以1.2等于4.14，然后将结果加上2.3，最终答案为6.44。');
INSERT INTO `calculate_question` VALUES (23, '3.45 + 2.78 * 1.5 - 4.12 =', 'test', '3', '2024-12-31 16:21:21.148417', '3.50', '', '', '解析：首先计算乘法部分，即2.78 * 1.5 = 4.17。然后按照从左到右的顺序进行加减运算，即3.45 + 4.17 - 4.12 = 7.62 - 4.12 = 3.50。');
INSERT INTO `calculate_question` VALUES (24, '计算：5/6 + 3/4 - 1/3 =', 'test', '3', '2024-12-31 16:24:16.212602', '5/4', '', '', '解析：首先找到所有分数的最小公倍数，这里是12。然后将每个分数转换为以12为分母的分数：5/6 = 10/12，3/4 = 9/12，1/3 = 4/12。接着进行加减运算：10/12 + 9/12 - 4/12 = 15/12。最后，将15/12化简为最简分数，得到5/4。');
INSERT INTO `calculate_question` VALUES (25, '计算：(3/4 - 1/8) * 6 =', 'test', '3', '2024-12-31 16:24:26.350889', '3.75', '', '', '解析：首先计算括号内的分数减法，3/4 - 1/8 = 6/8 - 1/8 = 5/8。然后将结果乘以6，5/8 * 6 = 30/8 = 15/4 = 3.75。');
INSERT INTO `calculate_question` VALUES (26, '3.2 * (5.1 + 2.9) / 2.5 =', 'test', '3', '2024-12-31 16:24:35.977050', '10.24', '', '', '解析：首先计算括号内的加法，5.1 + 2.9 = 8.0，然后进行乘法运算，3.2 * 8.0 = 25.6，最后进行除法运算，25.6 / 2.5 = 10.24');
INSERT INTO `calculate_question` VALUES (27, '计算：(3/4 + 2/3) * (5/6 - 1/2) =', 'test', '3', '2024-12-31 16:25:28.202584', '17/36', '', '', '解析：首先计算括号内的分数加减，3/4 + 2/3 = 9/12 + 8/12 = 17/12，5/6 - 1/2 = 5/6 - 3/6 = 2/6 = 1/3。然后计算两个结果的乘积，17/12 * 1/3 = 17/36。');
INSERT INTO `calculate_question` VALUES (28, '计算：(5/6 + 3/4) * (7/8 - 1/2)', 'test', '3', '2024-12-31 16:25:45.305220', '19/32', '', '', '解析：首先，计算括号内的分数加减。5/6 + 3/4，需要找到最小公倍数12，得到(10/12 + 9/12) = 19/12。7/8 - 1/2，需要找到最小公倍数8，得到(7/8 - 4/8) = 3/8。然后，将两个结果相乘，19/12 * 3/8 = (19 * 3) / (12 * 8) = 57/96。最后，简化分数，57/96可以约分，分子分母同时除以3，得到19/32。');

-- ----------------------------
-- Table structure for essay_question
-- ----------------------------
DROP TABLE IF EXISTS `essay_question`;
CREATE TABLE `essay_question`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `question` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `index` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `generate_time` datetime(6) NULL DEFAULT NULL,
  `solution` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `user_answer` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `flag` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `comment` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of essay_question
-- ----------------------------
INSERT INTO `essay_question` VALUES (1, '一个农场主有30亩的草地，用来饲养牛和羊。每头牛需要占用0.5亩草地，每只羊需要占用0.2亩草地。如果农场主希望饲养的牛和羊的总头数不超过80头，且草地刚好用完，那么农场主最多可以饲养多少头牛？', 'test', '2', '2024-12-30 21:16:59.523339', '设农场主饲养的牛数量为x，羊的数量为y。根据题意得出以下方程组：x + y ≤ 80；0.5x + 0.2y = 30。将y表示为y = 80 - x，代入第二个方程：0.5x + 0.2(80 - x) = 30，化简得0.5x + 16 - 0.2x = 30，整理后得0.3x = 14，解得x ≈ 46.67。因为牛的数量不能为小数，所以农场主最多可以饲养46头牛。', '987', 'false', '解析：这道题目涉及到多变量方程的求解，需要根据草地的总面积和每种动物所需的草地面积，以及动物总数量不超过80头的限制，来求解最多可以饲养的牛的数量。通过设立一对方程，将其中一个变量表示为另一个变量的函数，并代入求解，最终得到牛的最大饲养数量。');
INSERT INTO `essay_question` VALUES (2, '某学校图书馆购进了若干本小说和科普书，共花费了450元。已知每本小说价格为25元，每本科普书价格为15元，且购买的小说数量是科普书的2倍。问学校购买了多少本小说和科普书？', 'test', '2', '2024-12-30 21:17:19.765022', '解：设学校购买了x本科普书，则购买了2*x本小说。15*x + 25*(2*x) = 450，15*x + 50*x = 450，65*x = 450，x ≈ 6.92。因为书籍数量必须是整数，所以x=7。2*x=14。答：学校购买了14本小说和7本科普书。', NULL, 'false', '解析：设科普书数量为x，根据题意，小说数量为2x。根据总花费建立方程：15x + 25(2x) = 450。简化方程得到：65x = 450，解得：x ≈ 6.92。由于书籍数量必须是整数，故x取7。因此，小说数量为14本，科普书数量为7本。');
INSERT INTO `essay_question` VALUES (4, '一块长方形的地毯，长为5.2米，宽为3.6米，现在要将其裁剪成若干个边长为0.4米的正方形小地毯，可以裁剪出多少块这样的小地毯？', 'test', '2', '2024-12-30 21:17:50.571428', '5.2*3.6/(0.4*0.4)=117(块)', '解：\r\n答：', 'false', '解析：首先计算长方形地毯的面积，即长乘以宽，得到5.2*3.6=18.72平方米。然后计算每个正方形小地毯的面积，即边长乘以边长，得到0.4*0.4=0.16平方米。最后将长方形地毯的面积除以每个正方形小地毯的面积，得到18.72/0.16=117块。');
INSERT INTO `essay_question` VALUES (5, '在一个花园里，有50株玫瑰、30株百合和20株郁金香。如果园丁随机选择一株花进行修剪，选择修剪玫瑰的可能性比百合大，但比郁金香小，那么至少需要再加入多少株玫瑰？', 'test', '2', '2024-12-30 21:18:07.150477', '至少需要再加入11株玫瑰。', '11', 'true', '解析：首先计算当前各种花的选择概率。玫瑰的概率为50/(50+30+20)=50/100=1/2，百合的概率为30/100=3/10，郁金香的概率为20/100=1/5。根据题目要求，玫瑰的选择概率应大于百合但小于郁金香，即3/10 < 玫瑰的概率 < 1/5。为了满足这个条件，需要增加玫瑰的数量。设增加x株玫瑰，新的玫瑰概率为(50+x)/(100+x)。解不等式3/10 < (50+x)/(100+x) < 1/5，得到x > 10。因此，至少需要再加入11株玫瑰。');
INSERT INTO `essay_question` VALUES (6, '某工厂生产了A、B两种产品共1000件，其中A产品的数量比B产品的3倍多40件。求A、B两种产品各生产了多少件？', 'test', '2', '2024-12-30 21:18:25.378489', '解：设B产品的数量为x件，则A产品的数量为(3*x + 40)件。x + (3*x + 40) = 1000，4*x + 40 = 1000，4*x = 960，x = 240。3*x + 40 = 3*240 + 40 = 760。答：A产品生产了760件，B产品生产了240件。', '解：', 'false', '解析：设B产品的数量为x件，则A产品的数量为(3*x + 40)件。根据题意，x + (3*x + 40) = 1000，即4*x + 40 = 1000。解方程得4*x = 960，x = 240。因此，3*x + 40 = 3*240 + 40 = 760。所以，A产品生产了760件，B产品生产了240件。');
INSERT INTO `essay_question` VALUES (9, '小明和小红一起购买了40个苹果，小明购买了全部苹果的2/5，小红购买了全部苹果的1/4。他们还剩下多少个苹果？', 'test', '3', '2024-12-31 16:25:58.309390', '40-40*2/5-40*1/4=14(个)', '', '', '解析：首先计算小明和小红购买的苹果数量，然后从总数中减去他们购买的苹果数量，得到剩下的苹果数量。计算过程为：小明购买的苹果数量为40 * 2/5 = 16个，小红购买的苹果数量为40 * 1/4 = 10个，剩下的苹果数量为40 - 16 - 10 = 14个。');
INSERT INTO `essay_question` VALUES (10, '张先生需要用30米的绳子围成一个矩形花坛，其中一边的长度是6米，其他三边应该分别多长？', 'test', '3', '2024-12-31 16:26:12.543780', '设矩形花坛的另一边长度为x米。根据矩形的周长公式，2*(长+宽)=周长，即2*(6+x)=30。解方程得x=9米。因此，其他三边的长度分别为9米、6米和9米。', '', '', '解析：根据矩形的周长公式，2*(长+宽)=周长，将已知的长度和周长代入公式，求出未知边的长度。这样就可以确定其他三边的长度。');
INSERT INTO `essay_question` VALUES (11, '李阿姨买了一些苹果和香蕉，总共花了45元。已知每千克苹果的价格是3元，每千克香蕉的价格是5元。李阿姨买苹果和香蕉的总重量是10千克，且买苹果的重量是买香蕉重量的2倍。请问李阿姨买了多少千克苹果和多少千克香蕉？', 'test', '3', '2024-12-31 16:26:36.311113', '设李阿姨买了x千克苹果和y千克香蕉。根据题意，x = 2y，x + y =10。解方程得y = 10/3，x = 20/3。李阿姨买了20/3千克苹果和10/3千克香蕉。', '', '', '解析：设李阿姨买了x千克苹果和y千克香蕉。根据题意，x + y =10，且x = 2y。将x = 2y代入x + y =10，得到3y =10，即y = 10/3。再将y = 10/3代入x = 2y，得到x = 20/3。因此，李阿姨买了20/3千克苹果和10/3千克香蕉。');
INSERT INTO `essay_question` VALUES (12, '李阿姨在水果店买了4.5千克的苹果和3.75千克的香蕉。已知每千克苹果的价格是6.8元，每千克香蕉的价格是4.2元。李阿姨付给店员100元，店员应找给李阿姨多少元？', 'test', '3', '2024-12-31 16:27:04.768876', '李阿姨购买的苹果的总价是4.5千克 * 6.8元/千克 = 30.6元。香蕉的总价是3.75千克 * 4.2元/千克 = 15.75元。苹果和香蕉的总价是30.6元 + 15.75元 = 46.35元。李阿姨付给店员100元，店员应找给李阿姨100元 - 46.35元 = 53.65元。所以店员应找给李阿姨53.65元。', '', '', '解析：首先计算李阿姨购买的苹果和香蕉的总价，然后将总价从李阿姨支付的100元中减去，得到店员应找的金额。');
INSERT INTO `essay_question` VALUES (13, '一家餐厅有35位顾客，每位顾客都点了2.5升的水。餐厅的水桶容量是45升。请问餐厅至少需要准备多少桶水？', 'test', '3', '2024-12-31 16:27:18.593304', '35位顾客共需要水的总量是35*2.5=87.5升。每桶水45升，87.5除以45等于1.944，向上取整得2。所以餐厅至少需要准备2桶水。', '', '', '解析：首先计算所有顾客需要的水的总量，然后将总量除以水桶的容量，得到的结果向上取整，即为至少需要准备的水桶数量。');
INSERT INTO `essay_question` VALUES (14, '农场主有108只鸡和90只鸭，他希望将它们平均分配到若干个笼子里，每个笼子里的鸡和鸭的数量相等且尽可能多。问：农场主最多可以分成多少个笼子？每个笼子里有多少只鸡和鸭？', 'test', '3', '2024-12-31 16:27:32.311309', '108和90的最大公因数是18。108/18=6(只), 90/18=5(只), 答：农场主最多可以分成18个笼子，每个笼子里有6只鸡和5只鸭。', '', '', '解析：这道题目考察的是最大公因数的应用。首先，我们需要找到108和90的最大公因数，这个最大公因数就是农场主可以分成的笼子数。然后，我们将鸡和鸭的数量分别除以这个最大公因数，就可以得到每个笼子里鸡和鸭的数量。');

-- ----------------------------
-- Table structure for fill_question
-- ----------------------------
DROP TABLE IF EXISTS `fill_question`;
CREATE TABLE `fill_question`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `question` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `index` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `generate_time` datetime(6) NULL DEFAULT NULL,
  `solution` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `user_answer` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `flag` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `comment` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 81 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fill_question
-- ----------------------------
INSERT INTO `fill_question` VALUES (1, '一位农民种植西红柿，每平方米可以收获2.5千克。他有一块地，面积为50平方米，这块地可以收获(  )千克西红柿。', 'test', '2', '2024-12-30 21:14:21.041528', '125', '125', 'true', '解析：首先，我们需要计算这块地总共可以收获多少千克西红柿。已知每平方米可以收获2.5千克，所以50平方米可以收获的总量就是每平方米的收获量乘以总面积。计算过程为2.5千克/平方米 * 50平方米 = 125千克。因此，这块地可以收获125千克西红柿。');
INSERT INTO `fill_question` VALUES (2, '某工厂使用一台机器加工零件，这台机器5小时可以加工35.75个零件。如果该机器的工作效率保持不变，那么它加工28.6个零件需要的时间是(  )小时。', 'test', '2', '2024-12-30 21:14:31.536324', '4', '4', 'true', '解析：首先计算这台机器每小时加工零件的效率，即35.75个零件除以5小时，得到每小时加工7.15个零件。然后根据这个效率计算加工28.6个零件所需的时间，即28.6个零件除以每小时加工7.15个零件，得到4小时。');
INSERT INTO `fill_question` VALUES (3, '一桶果汁重18.5千克，每千克售价6.8元，这桶果汁的总售价是(  )元。', 'test', '2', '2024-12-30 21:14:39.597672', '125.8', '125.8', 'true', '解析：根据题目，果汁的总重量为18.5千克，每千克的售价为6.8元。计算总售价的方法是将总重量乘以每千克的售价。因此，计算过程为18.5 * 6.8，结果为125.8元。');
INSERT INTO `fill_question` VALUES (4, '某超市进行促销活动，原价每千克10元的苹果现在打8折出售。小明购买了2.5千克的苹果，他需要支付的金额是(  )元。', 'test', '2', '2024-12-30 21:14:50.349704', '20', '20', 'true', '解析：首先计算打折后的苹果单价，即10元/千克乘以0.8得到8元/千克。然后计算小明购买2.5千克苹果的总金额，即8元/千克乘以2.5千克得到20元。');
INSERT INTO `fill_question` VALUES (5, '在一条长180米的公路一侧栽树(两端都不栽)，每隔9米栽一棵，一共要栽(   )棵。', 'test', '2', '2024-12-30 21:14:59.038237', '19', '19', 'true', '解析：根据两端都不栽的植树问题公式，总棵数=总长度/间隔距离-1。因此，180米除以9米得到20，再减去1得到19棵。');
INSERT INTO `fill_question` VALUES (6, '一个梯形的面积是36平方厘米，下底是10厘米，上底是6厘米，高是(  )厘米。', 'test', '2', '2024-12-30 21:15:08.837113', '6', '6', 'true', '解析：根据梯形面积公式，面积 = (上底 + 下底) × 高 ÷ 2。已知面积为36平方厘米，上底为6厘米，下底为10厘米，代入公式得36 = (6 + 10) × 高 ÷ 2，解得高 = 6厘米。');
INSERT INTO `fill_question` VALUES (7, '一个农场主种植了小麦和玉米，两种作物的总种植面积是520亩，其中小麦的种植面积比玉米的2倍少20亩，玉米的种植面积是(  )亩。', 'test', '2', '2024-12-30 21:15:18.475877', '200', '200', 'true', '解析：设玉米的种植面积为x亩，则小麦的种植面积为(2*x-20)亩。根据题意，x+(2*x-20)=520，整理得3*x-20=520，解得x=200。因此，玉米的种植面积是200亩。');
INSERT INTO `fill_question` VALUES (8, '在一个装有6个红球和4个蓝球的袋子中，随机取出一个小球并记录颜色，取出后不再放回。第一次取出红球的概率是(  )。如果第一次取出的红球，那么第二次取出蓝球的概率是(  )。', 'test', '2', '2024-12-30 21:15:28.449308', '3/5，2/9', '3/5，2/9', 'true', '解析：第一次取出红球的概率是6个红球除以总的10个球，即6/10=3/5。如果第一次取出的红球，那么袋中剩下5个红球和4个蓝球，总共9个球。因此，第二次取出蓝球的概率是4/9。');
INSERT INTO `fill_question` VALUES (9, '在一个装有15个红球、10个蓝球和5个黄球的袋子中，小李每次随机取出2个球并记录颜色，取出后不再放回。第一次取出两个红球的概率是(  )。', 'test', '2', '2024-12-30 21:15:39.482647', '91/285', '91', 'false', '解析：第一次取出两个红球的概率是组合数C(15,2)除以总的组合数C(30,2)，即(15*14/2)/(30*29/2)=105/435=21/87=7/29=91/285。');
INSERT INTO `fill_question` VALUES (10, '一家水果店以每千克2.8元的价格购入苹果，花费了86.8元。如果将这些苹果每3.5千克装一袋，可以装(  )袋。', 'test', '2', '2024-12-30 21:15:47.511597', '9', '9', 'true', '解析：首先计算购入的苹果总重量，即86.8除以2.8得到31千克。然后将总重量31千克除以每袋装的3.5千克，得到可以装的袋数为9。');
INSERT INTO `fill_question` VALUES (71, '有18个外观相同的橙子，其中有一个橙子比其他橙子轻一些。利用天平称重，至少需要称(   )次才能保证找出这个轻的橙子。', 'test', '3', '2024-12-31 16:16:35.192137', '3', '', '', '解析：将18个橙子分成3组，每组6个。第一次称重，比较其中两组。如果天平平衡，则轻的橙子在剩下的第三组中；如果不平衡，轻的橙子在较轻的一组中。第二次称重，将较轻的一组中的6个橙子分成两组，每组3个，比较其中两组。如果天平平衡，则轻的橙子在剩下的第三组中；如果不平衡，轻的橙子在较轻的一组中。第三次称重，将较轻的一组中的3个橙子分成两组，每组1个，比较其中两组。如果天平平衡，则剩下的1个橙子是轻的；如果不平衡，轻的橙子就是较轻的那个。因此，至少需要称3次才能保证找出轻的橙子。');
INSERT INTO `fill_question` VALUES (72, '一个长方体的水箱，长是3米，宽是2米，高是1.5米。现在水箱中装有水，水深是1米。如果将水箱倾斜，使最小的面朝下，水深变为(  )米。', 'test', '3', '2024-12-31 16:16:47.582241', '1.5', '', '', '解析：首先计算水箱的体积，3*2*1.5=9立方米。然后计算水箱中水的体积，3*2*1=6立方米。当水箱倾斜使最小的面朝下时，水的体积不变，新的水深为6/(2*1.5)=1.5米。');
INSERT INTO `fill_question` VALUES (73, '一个长方体水槽，长8米，宽6米，高4米。用水管向其中注水，注水速度为每分钟5立方米。水槽注满所需的时间是(  )小时。', 'test', '3', '2024-12-31 16:17:02.021095', '6.4', '', '', '解析：首先计算长方体水槽的体积，8*6*4=192(立方米)。然后计算注满水槽所需的时间，192/5=38.4(分钟)。最后将时间转换为小时，38.4/60=0.64(小时)。答案：水槽注满所需的时间是6.4小时。');
INSERT INTO `fill_question` VALUES (74, '某超市运来西瓜4/5吨，比运来的哈密瓜少1/10吨。运来的哈密瓜有(  )吨。', 'test', '3', '2024-12-31 16:17:13.901005', '9/10', '', '', '解析：首先根据题意，运来的西瓜比哈密瓜少1/10吨，因此哈密瓜的重量是西瓜的重量加上1/10吨。西瓜的重量是4/5吨，所以哈密瓜的重量是4/5 + 1/10。计算时需要将两部分分数转换为相同的分母，即4/5 = 8/10，所以8/10 + 1/10 = 9/10吨。因此运来的哈密瓜有9/10吨。');
INSERT INTO `fill_question` VALUES (75, '一个长方体蓄水池，长10米，宽5米，高3米。池内原有水深1.5米，现向池中注入水，使水深增加到2.5米。注入的水量为(  )立方米。', 'test', '3', '2024-12-31 16:17:24.655607', '50', '', '', '解析：首先计算注入水后的总水量，10*5*2.5=125立方米。然后计算原有水量，10*5*1.5=75立方米。最后计算注入的水量，125-75=50立方米。');
INSERT INTO `fill_question` VALUES (76, '一个长方体的水箱，长3米，宽2.5米，高2米。现将水箱装满水，然后将水倒入一个长5米，宽2米，高1.5米的长方体水池中，水池中的水深是(  )米。', 'test', '3', '2024-12-31 16:17:38.681850', '0.6', '', '', '解析：首先计算水箱的容积，即3*2.5*2=15立方米。然后将这15立方米的水倒入水池中，水池的底面积为5*2=10平方米。所以水池中的水深为15/10=1.5米。');
INSERT INTO `fill_question` VALUES (77, '一个长方体水箱，长8米，宽5米，高4米，内部装满了水。如果将这些水倒入一个边长为6米的正方体水箱中，正方体水箱中会剩余(  )立方米的空间。', 'test', '3', '2024-12-31 16:17:54.553792', '44', '', '', '解析：首先计算长方体水箱的体积，8*5*4=160立方米。然后计算正方体水箱的体积，6*6*6=216立方米。最后计算正方体水箱中剩余的空间，216-160=44立方米。答案：正方体水箱中会剩余44立方米的空间。');
INSERT INTO `fill_question` VALUES (78, '有20个外观相同的苹果，其中的19个质量相同，另有一个略轻一些。用天平称，至少称(  )次就一定能找出较轻的苹果。', 'test', '3', '2024-12-31 16:18:06.843146', '3', '', '', '解析：根据分组称重法，首先将20个苹果平均分成三组，分别为7个、7个和6个。第一次称重比较两组7个的苹果，如果平衡，则较轻的苹果在剩下的6个中；如果不平衡，则较轻的苹果在较轻的一组中。对于剩下的苹果，继续平均分组称重，每次可以排除三分之二的苹果，因此，经过3次称重，可以确保找出较轻的苹果。');
INSERT INTO `fill_question` VALUES (79, '一架天平最多只能称4次，有26个外观相同的橘子，其中有一个橘子比其他橘子轻一些。最少需要称( )次才能保证找出那个轻的橘子。', 'test', '3', '2024-12-31 16:18:20.463575', '4', '', '', '解析：题目中提到有26个橘子，要找出其中较轻的一个，且最多只能称4次。根据称量找次品的策略，每次称量可以将物品分成三组，这样可以最大限度地减少称量次数。首先，将26个橘子分成三组，分别为9个、9个和8个。第一次称量比较两组9个的橘子，如果平衡，则轻的橘子在剩下的8个中；如果不平衡，则轻的橘子在较轻的一组中。接着，根据第一次称量的结果，进一步将较少的部分分成三组，继续称量。如此反复，直到找到轻的橘子。由于每次称量都能将范围缩小到原来的三分之一，因此最少需要称4次才能保证找出那个轻的橘子。');
INSERT INTO `fill_question` VALUES (80, '小明买了一袋5斤的苹果，第一天吃了2/5斤，第二天吃了1/4斤，第三天又买进了1/3斤。现在小明手里还有(  )斤苹果。', 'test', '3', '2024-12-31 16:21:11.894223', '37/60', '', '', '解析：首先，计算小明第一天和第二天吃掉的苹果总量：2/5 + 1/4 = 8/20 + 5/20 = 13/20斤。然后，计算三天后的苹果总量：5 - 13/20 + 1/3 = 5 - 0.65 + 0.333... = 4.683...斤。最后，将结果转换为分数形式：4.683... ≈ 37/60斤。因此，小明手里还有37/60斤苹果。');

-- ----------------------------
-- Table structure for generate_record
-- ----------------------------
DROP TABLE IF EXISTS `generate_record`;
CREATE TABLE `generate_record`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `index` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `question_range` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `total_score` float NULL DEFAULT NULL,
  `user_score` float NULL DEFAULT NULL,
  `select_score` float NULL DEFAULT NULL,
  `judge_score` float NULL DEFAULT NULL,
  `fill_score` float NULL DEFAULT NULL,
  `calculate_score` float NULL DEFAULT NULL,
  `essay_score` float NULL DEFAULT NULL,
  `comment` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `generate_time` datetime(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 28 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of generate_record
-- ----------------------------
INSERT INTO `generate_record` VALUES (1, 'test', '0', NULL, 0, 0, 0, 0, 0, 0, 0, NULL, NULL);
INSERT INTO `generate_record` VALUES (3, 'test', '2', '【单元测试】 五年级上册，第一单元', 94, 68, 20, 12, 18, 12, 6, '您的答题准确率约为72.3%，表现不错！继续保持努力，您一定能够取得更好的成绩。加油！', '2024-12-30 21:10:40.448349');
INSERT INTO `generate_record` VALUES (27, 'test', '3', '【综合测试】 五年级上册', 100, 0, 0, 0, 0, 0, 0, '', '2024-12-31 16:11:59.717369');

-- ----------------------------
-- Table structure for judge_question
-- ----------------------------
DROP TABLE IF EXISTS `judge_question`;
CREATE TABLE `judge_question`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `question` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `index` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `generate_time` datetime(6) NULL DEFAULT NULL,
  `solution` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `user_answer` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `flag` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `comment` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 70 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of judge_question
-- ----------------------------
INSERT INTO `judge_question` VALUES (1, '在图书馆里，小明坐在第3列第5行的位置，用数对(3, 5)表示。小华坐在小明正右方的第二个位置，用数对表示为(5, 5)。实际上，小华的位置应该是(4, 5)，因为每向右移动一个位置，列数加1。', 'test', '2', '2024-12-30 21:13:21.154455', 'false', 'false', 'true', '解析：根据题意，小明坐在第3列第5行，用数对(3, 5)表示。小华坐在小明正右方的第二个位置，即列数加2，行数不变。因此，小华的位置应该是(3+2, 5)，即(5, 5)。但题目中给出的小华的位置是(4, 5)，这与计算结果不符，因此题目错误。');
INSERT INTO `judge_question` VALUES (2, '某超市促销活动中，购买3瓶果汁需要支付8.25元，而购买5瓶果汁需要支付13.75元。据此可以推断，购买4瓶果汁的价格正好是11元。', 'test', '2', '2024-12-30 21:13:30.398774', 'true', 'true', 'true', '解析：首先计算购买1瓶果汁的价格，购买3瓶果汁需要支付8.25元，所以1瓶果汁的价格为8.25/3=2.75元。然后计算购买4瓶果汁的价格，4瓶果汁的价格为4*2.75=11元。因此，题目中的推断是正确的。');
INSERT INTO `judge_question` VALUES (3, '一个长方形的花坛，长20米，宽15米，沿四周每隔4米种一棵树（四个角各种一棵），则一共需要种14棵树。', 'test', '2', '2024-12-30 21:13:37.620077', 'false', 'false', 'true', '解析：首先计算长方形的周长，周长=(20+15)*2=70(米)。然后根据每隔4米种一棵树，计算树的数量，70/4=17.5，由于树的数量必须是整数，所以需要种18棵树。因此，题目中说的14棵树是不正确的。');
INSERT INTO `judge_question` VALUES (4, '一个矩形和一个梯形等底等高，矩形的面积是72平方厘米，梯形的上底比下底少3cm，梯形的面积是60平方厘米。', 'test', '2', '2024-12-30 21:13:51.025894', 'true', 'true', 'true', '解析：首先，矩形的面积计算公式为底乘以高，已知矩形的面积是72平方厘米，因为矩形和梯形等底等高，所以梯形的高也是相同的。梯形的面积计算公式为（上底+下底）乘以高除以2。已知梯形的上底比下底少3cm，设下底为x cm，则上底为(x-3) cm。根据梯形面积公式，我们可以得到方程：((x-3)+x)*高/2=60。由于矩形和梯形等高，我们可以得到高=72/底。将高代入梯形面积公式，解方程得到x=13.5 cm。然后计算梯形的面积，得到60平方厘米。因此，题目中的描述是正确的。');
INSERT INTO `judge_question` VALUES (5, '某水电站一天的发电量为234500千瓦时，若每千瓦时的电费为0.6元，则该水电站一天的发电收入为140700元。', 'test', '2', '2024-12-30 21:13:58.179493', 'true', 'true', 'true', '解析：计算水电站一天的发电收入，可以将一天的发电量234500千瓦时乘以每千瓦时的电费0.6元，得到的结果为140700元。');
INSERT INTO `judge_question` VALUES (6, '某超市促销活动中，购买3瓶果汁和5盒牛奶共花费58.5元，已知每瓶果汁售价为8.5元，每盒牛奶售价为7.5元。', 'test', '2', '2024-12-30 21:14:12.013787', 'false', 'false', 'true', '解析：根据题目，购买3瓶果汁和5盒牛奶共花费58.5元，已知每瓶果汁售价为8.5元，每盒牛奶售价为7.5元。我们可以先计算3瓶果汁的总价，即3*8.5=25.5元，然后用总花费58.5元减去果汁的总价25.5元，得到牛奶的总价为58.5-25.5=33元。最后用牛奶的总价33元除以5盒，得到每盒牛奶的售价为33/5=6.6元。由于题目中每盒牛奶的售价为7.5元，与计算结果6.6元不符，因此题目描述错误。');
INSERT INTO `judge_question` VALUES (64, '李叔叔买了12千克的苹果和15千克的梨，他发现这些水果的总重量是26.5千克。', 'test', '3', '2024-12-31 16:15:08.660782', 'false', '', '', '解析：李叔叔买的苹果和梨的总重量应该是12+15=27千克，而不是26.5千克。');
INSERT INTO `judge_question` VALUES (65, '某仓库内有12瓶装满水的水瓶，其中11瓶水的质量相同，剩下一瓶水的质量稍重一些。利用天平称，至少称3次即可保证找出较重的水瓶。', 'test', '3', '2024-12-31 16:15:25.045640', 'true', '', '', '解析：根据二分法原理，每次称重可以将水瓶数量大致分为三等份。对于12瓶水，第一次称重可以将12瓶分为4瓶、4瓶、4瓶三组，任意称其中两组，若天平平衡则次品在剩下的4瓶中，若不平衡则次品在较重的一组中。第二次称重则可以在剩下的4瓶中再分为1瓶、1瓶、2瓶三组，重复上述步骤。第三次称重可以直接比较最后两瓶或确定次品位置。因此，称3次即可保证找出较重的水瓶。');
INSERT INTO `judge_question` VALUES (66, '有9枚外观相同的金币，其中有一枚是假的，比真金币轻一些。使用天平称两次，不能保证一定能找出假金币。', 'test', '3', '2024-12-31 16:15:35.184081', 'false', '', '', '解析：将9枚金币分成3组，每组3枚。第一次称量，比较其中两组。如果天平平衡，假金币在剩下的那一组；如果不平衡，假金币在较轻的那一组。第二次称量，从疑似含有假金币的那一组中取出两枚进行比较。如果平衡，剩下的那一枚是假金币；如果不平衡，较轻的那一枚是假金币。因此，使用天平称两次，可以保证找出假金币。');
INSERT INTO `judge_question` VALUES (67, '一个长方体木箱，长3米，宽2米，高1.5米，里面装满了水。如果将这些水倒入一个边长为2.5米的正方体水箱中，正方体水箱中会剩余的空间为18.75立方米。', 'test', '3', '2024-12-31 16:15:53.308581', 'false', '', '', '解析：首先计算长方体木箱的体积，3*2*1.5=9(立方米)。然后计算正方体水箱的体积，2.5*2.5*2.5=15.625(立方米)。最后计算正方体水箱中剩余的空间，15.625-9=6.625(立方米)。题目中给出的剩余空间为18.75立方米，与计算结果不符。');
INSERT INTO `judge_question` VALUES (68, '一段木头被切成8段，每段的长度相等。然后从每段中切出1/4的长度作为雕刻材料，剩下的每段长度为原来的3/4。如果这段木头原来的总长度是8米，雕刻材料的总长度是2米。', 'test', '3', '2024-12-31 16:16:07.851673', 'true', '', '', '解析：这段木头的总长度为8米，被切成8段，每段长度为8/8=1米。从每段中切出1/4的长度作为雕刻材料，每段的雕刻材料长度为1*(1/4)=0.25米，8段的雕刻材料总长度为8*0.25=2米。剩下的每段长度为1*(3/4)=0.75米，符合题意。');
INSERT INTO `judge_question` VALUES (69, '小明有10支铅笔，小红有8支铅笔，他们一起把铅笔分给了3个小朋友。每个小朋友得到的铅笔数都是奇数。', 'test', '3', '2024-12-31 16:16:17.167207', 'false', '', '', '解析：小明和小红一共有18支铅笔，3个奇数相加的和是奇数，而18是偶数，所以不可能每个小朋友都得到奇数支铅笔。');

-- ----------------------------
-- Table structure for select_question
-- ----------------------------
DROP TABLE IF EXISTS `select_question`;
CREATE TABLE `select_question`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `question` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `index` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `generate_time` datetime(6) NULL DEFAULT NULL,
  `solution` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `option_a` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `option_b` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `option_c` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `option_d` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `user_answer` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `flag` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `comment` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 191 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of select_question
-- ----------------------------
INSERT INTO `select_question` VALUES (10, '小明买了5本数学书和3本文科书，共花了120元。已知每本数学书比每本文科书贵4元，求每本文科书的价格。', 'test', '2', '2024-12-30 21:11:03.800420', '12.5', '15', '17.5', '10', '12.5', '12.5', 'true', '解析：设每本文科书的价格为x元，则每本数学书的价格为(x+4)元。根据题意，有方程5*(x+4)+3*x=120，即5*x+20+3*x=120，8*x=100，x=12.5。所以每本文科书的价格是12.5元。');
INSERT INTO `select_question` VALUES (11, '在一场表演中，小李的位置用数对(3, 5)表示，小张的位置用数对(7, 5)表示，小王的位置用数对(5, 9)表示。如果小李和小张在同一排，那么小王和小李之间隔了多少排？', 'test', '2', '2024-12-30 21:11:16.060866', '4', '5', '4', '6', '3', '4', 'true', '解析：根据数对的定义，第一个数字表示列，第二个数字表示排。小李的位置是第3列第5排，小张的位置是第7列第5排，说明他们在同一排。小王的位置是第5列第9排，与小李的第5排相差4排。因此，小王和小李之间隔了4排。');
INSERT INTO `select_question` VALUES (12, '在一场比赛中，选手A的位置用数对表示为(5, 7)，选手B在选手A的正前方两个位置，选手C在选手B的正右方三个位置。请问选手C的位置用数对表示是多少？', 'test', '2', '2024-12-30 21:11:31.351014', '(8, 5)', '(8, 5)', '(7, 5)', '(8, 6)', '(5, 8)', '(8, 5)', 'true', '解析：选手A的位置是(5, 7)，选手B在选手A的正前方两个位置，所以选手B的列数不变，行数减2，即(5, 7-2) = (5, 5)。选手C在选手B的正右方三个位置，所以选手C的行数不变，列数加3，即(5+3, 5) = (8, 5)。');
INSERT INTO `select_question` VALUES (13, '某水果店有苹果和橙子共150千克，其中苹果的重量是橙子的1.5倍。苹果和橙子各有多少千克？', 'test', '2', '2024-12-30 21:11:43.118252', '90', '70', '100', '90', '80', '90', 'true', '解析：设橙子的重量为x千克，那么苹果的重量为1.5*x千克。根据题意，x+1.5*x=150，2.5*x=150，x=60，1.5*x=90。因此，橙子的重量是60千克，苹果的重量是90千克。');
INSERT INTO `select_question` VALUES (14, '某书店购进了小说和传记共120本，其中小说的数量是传记的3倍少10本。请问小说和传记各购进了多少本？', 'test', '2', '2024-12-30 21:11:56.656595', '传记33本，小说89本', '传记34本，小说88本', '传记33本，小说89本', '传记32本，小说88本', '传记32本，小说86本', '传记33本，小说89本', 'true', '解析：设传记的数量为x本，则小说的数量为(3*x-10)本。根据题意，x + (3*x - 10) = 120，4*x - 10 = 120，4*x = 130，x = 32.5。由于书籍数量不能为小数，因此传记购进了33本，小说购进了(3*33-10)=89本。');
INSERT INTO `select_question` VALUES (15, '一条街道长240米，沿一侧每隔12米安装一盏路灯（两端都安装），一共需要安装多少盏路灯？', 'test', '2', '2024-12-30 21:12:06.167413', '21', '20', '22', '21', '19', '21', 'true', '解析：街道两端都安装路灯，所以路灯的数量等于街道长度除以间隔距离再加1。计算过程为：240/12+1=21盏。');
INSERT INTO `select_question` VALUES (16, '一家果园种植了2400棵果树，其中苹果树占30%，梨树占25%，其余为桃树。果园主计划将苹果树以每棵3.5元的价格出售，梨树以每棵2.8元的价格出售，桃树以每棵2.2元的价格出售。请问果园主通过出售这些果树总共能获得多少收入？', 'test', '2', '2024-12-30 21:12:25.525434', '6576', '6480', '6624', '6576', '6500', '6576', 'true', '解析：首先计算各种果树的数量，苹果树数量为2400*0.3=720棵，梨树数量为2400*0.25=600棵，桃树数量为2400-720-600=1080棵。然后计算各种果树的收入，苹果树收入为720*3.5=2520元，梨树收入为600*2.8=1680元，桃树收入为1080*2.2=2376元。最后将三种果树的收入相加，总收入为2520+1680+2376=6576元。');
INSERT INTO `select_question` VALUES (17, '在一个书架上，有15本小说和10本非小说类书籍。如果从中随机取出一本书，取到小说的可能性比非小说大，那么至少需要再加入多少本小说？', 'test', '2', '2024-12-30 21:12:38.932062', '6', '6', '7', '8', '5', '6', 'true', '解析：要使取到小说的可能性比非小说大，小说的数量必须大于非小说的数量。目前小说有15本，非小说有10本，所以小说的数量至少要比非小说多1本。因此，需要再加入的小说数量为10 + 1 - 15 = 6本。');
INSERT INTO `select_question` VALUES (18, '在一个圆形花坛的周围，每隔4米种一棵树，一共种了20棵。如果改为每隔5米种一棵树，会少种多少棵树？', 'test', '2', '2024-12-30 21:12:54.572406', '4', '5', '3', '6', '4', '4', 'true', '解析：圆形花坛的周长可以通过树的数量和间隔计算得出，即周长=（树的数量-1）*间隔。原来的周长为（20-1）*4=76米。改为每隔5米种一棵树时，需要的树的数量为76/5+1=16棵。因此，会少种20-16=4棵树。');
INSERT INTO `select_question` VALUES (19, '一个梯形的花坛，上底是3.5米，下底是5.5米，高是2.5米。如果每平方米需要种植4株花，那么这个花坛一共需要种植多少株花？', 'test', '2', '2024-12-30 21:13:11.773664', '45', '50', '45', '40', '55', '45', 'true', '解析：首先计算梯形的面积，梯形面积公式为(上底+下底)*高/2，即(3.5+5.5)*2.5/2=11.25平方米。然后根据每平方米需要种植4株花，计算总株数为11.25*4=45株。');
INSERT INTO `select_question` VALUES (181, '小明有1瓶水，他第一天喝了这瓶水的3/8，第二天喝了这瓶水的1/4。还剩下这瓶水的几分之几没有喝？', 'test', '3', '2024-12-31 16:12:17.340335', '3/8', '5/8', '1/4', '1/2', '3/8', '', '', '解析：首先，我们需要计算小明两天一共喝了多少水。第一天喝了3/8，第二天喝了1/4。我们需要将这两个分数相加，然后从1中减去这个和，得到剩下的水的比例。3/8 + 1/4 = 3/8 + 2/8 = 5/8。然后，1 - 5/8 = 3/8。所以，小明还剩下这瓶水的3/8没有喝。');
INSERT INTO `select_question` VALUES (182, '小华家有120度电，她计划将这些电分成若干份，每份电的数量都是4的倍数。请问她最多可以分成多少份？', 'test', '3', '2024-12-31 16:12:29.230351', '30', '20', '30', '40', '50', '', '', '解析：要将120度电分成若干份，每份都是4的倍数，首先需要找出120度电中包含多少个4的倍数。因为120除以4等于30，所以最多可以分成30份。');
INSERT INTO `select_question` VALUES (183, '一个长方体玻璃缸，长8分米，宽6分米，高4分米，内部装满了水。如果将这些水倒入一个边长为5分米的正方体玻璃缸中，正方体玻璃缸中会剩余多少立方分米的空间？', 'test', '3', '2024-12-31 16:12:48.061982', '67', '60', '75', '67', '70', '', '', '解析：首先计算长方体玻璃缸的体积，8*6*4=192(立方分米)。然后计算正方体玻璃缸的体积，5*5*5=125(立方分米)。最后计算正方体玻璃缸中剩余的空间，192-125=67(立方分米)。答案：正方体玻璃缸中会剩余67立方分米的空间。');
INSERT INTO `select_question` VALUES (184, '一个长方体的储物柜，长3米，宽2米，高1.5米，内部有三个隔板，每个隔板都是1厘米厚的木板，将储物柜分成了四个相同大小的储物格。如果每个储物格内部高度相同，那么每个储物格的内部高度是多少米？', 'test', '3', '2024-12-31 16:13:04.352425', '1.47', '1.45', '1.47', '1.50', '1.48', '', '', '解析：首先计算储物柜的总体积，3*2*1.5=9立方米。然后计算三个隔板占据的体积，1厘米=0.01米，3*2*0.01*3=0.18立方米。储物柜的实际可用体积为9-0.18=8.82立方米。每个储物格的体积为8.82/4=2.205立方米。储物格的底面积为3*2/4=1.5平方米。因此，每个储物格的内部高度为2.205/1.5=1.47米。');
INSERT INTO `select_question` VALUES (185, '有20个外观相同的苹果，其中有一个苹果比其他苹果轻一些。你有一台天平，最多只能称4次。请问，最少需要称几次才能保证找出那个轻的苹果？', 'test', '3', '2024-12-31 16:13:22.979955', '4', '6', '4', '3', '5', '', '', '解析：首先，将20个苹果分成三组，分别为7个、7个和6个。第一次称重，比较两组7个的苹果，如果天平平衡，则轻的苹果在剩下的6个中；如果不平衡，则轻的苹果在较轻的一组中。接着，根据第一次称重的结果，将包含轻苹果的那一组继续分成三组，重复上述过程。每次称重都能将可能性减少到原来的三分之一，因此，通过4次称重，可以保证找出那个轻的苹果。');
INSERT INTO `select_question` VALUES (186, '有9个外观相同的包裹，其中有一个包裹比其他的轻一些。你有一台天平，最多只能称3次。请问，最少需要称几次才能保证找出那个轻的包裹？', 'test', '3', '2024-12-31 16:13:36.600335', '2', '1', '3', '4', '2', '', '', '解析：这个问题可以通过分组称重的方法来解决。首先，将9个包裹分成3组，每组3个包裹。第一次称重时，比较任意两组。如果两组重量相等，则轻的包裹在剩下的那组中；如果两组重量不等，则轻的包裹在较轻的那一组中。第二次称重时，将较轻的那一组中的3个包裹分成两组，每组1个包裹，再称一次。如果两组重量相等，则轻的包裹是剩下的那一个；如果两组重量不等，则轻的包裹在较轻的那一组中。这样，通过两次称重就可以保证找出那个轻的包裹。');
INSERT INTO `select_question` VALUES (187, '一个小组有10名学生，其中5名是男生，其他是女生。若将小组按性别分成两组，每组的平均人数是全组的几分之几？', 'test', '3', '2024-12-31 16:13:47.148013', '1/2', '3/4', '1/3', '1/2', '2/3', '', '', '解析：首先计算全组的总人数，即10名学生。然后将小组按性别分成两组，每组的平均人数是全组人数的一半，即10/2=5。所以每组的平均人数是全组的5/10，化简后为1/2。');
INSERT INTO `select_question` VALUES (188, '一家面包店有180个面包和240个蛋糕，店主想要将这些糕点分成若干盒，每盒中面包的数量相同，蛋糕的数量也相同。每盒中面包和蛋糕的总重量都是6的倍数。请问每盒中最多可以放入多少个面包和多少个蛋糕？', 'test', '3', '2024-12-31 16:14:03.430426', '60', '60', '50', '30', '40', '', '', '解析：首先，我们需要找到180和240的最大公约数，因为每盒中面包和蛋糕的数量必须相同。180和240的最大公约数是60。然后，我们需要确保每盒中面包和蛋糕的总重量是6的倍数。由于60是6的倍数，所以每盒中最多可以放入60个面包和60个蛋糕。');
INSERT INTO `select_question` VALUES (189, '有48个苹果，要把它们分成若干堆，每堆苹果的数量都是4的倍数。请问最多可以分成多少堆？', 'test', '3', '2024-12-31 16:14:15.718720', '12', '10', '12', '11', '13', '', '', '解析：首先计算48除以4的结果，得到12，因为每堆数量必须是4的倍数，所以最多可以分成12堆。');
INSERT INTO `select_question` VALUES (190, '一家超市有3/7吨的蔬菜，第一天卖掉了1/4吨，第二天卖掉了1/6吨。还剩下多少吨的蔬菜？', 'test', '3', '2024-12-31 16:15:00.366819', '1/84', '1/28', '1/84', '1/42', '1/14', '', '', '解析：首先，我们需要计算超市原本有的蔬菜总量，即3/7吨。然后，我们减去第一天卖掉的1/4吨和第二天卖掉的1/6吨。为了进行减法运算，我们需要找到一个共同的分母。3/7、1/4和1/6的共同分母是84。将每个分数转换为以84为分母的分数，我们得到36/84、21/84和14/84。然后，我们将这些分数相减：36/84 - 21/84 - 14/84 = 1/84。因此，还剩下1/84吨的蔬菜。');

-- ----------------------------
-- Table structure for setting
-- ----------------------------
DROP TABLE IF EXISTS `setting`;
CREATE TABLE `setting`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `progress` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `integrated_grade` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `select_flag` tinyint NULL DEFAULT NULL,
  `select_quantity` int NULL DEFAULT NULL,
  `judge_flag` tinyint NULL DEFAULT NULL,
  `judge_quantity` int NULL DEFAULT NULL,
  `fill_flag` tinyint NULL DEFAULT NULL,
  `fill_quantity` int NULL DEFAULT NULL,
  `calculate_flag` tinyint NULL DEFAULT NULL,
  `calculate_quantity` int NULL DEFAULT NULL,
  `essay_flag` tinyint NULL DEFAULT NULL,
  `essay_quantity` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `username`(`username` ASC) USING BTREE,
  CONSTRAINT `setting_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of setting
-- ----------------------------
INSERT INTO `setting` VALUES (1, 'test', 'grade5-1, unit1', 'grade5-2', 1, 10, 1, 6, 1, 10, 1, 6, 1, 6);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `token` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `create_time` datetime(6) NULL DEFAULT NULL,
  `login_time` datetime(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `constraint_user`(`username` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'test', 'c4ca4238a0b923820dcc509a6f75849b', '098f6bcd4621d373cade4e832627b4f6', '2024-12-30 21:05:38.642073', '2024-12-30 21:05:41.554002');

SET FOREIGN_KEY_CHECKS = 1;
