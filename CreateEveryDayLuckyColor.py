from ics import Calendar, Event
import datetime
import Lunar

# 五行对应关系
wuxing_colors = {
    "金": {
        "大吉": ["蓝", "黑", "灰"],
        "次吉": ["金", "银", "白"],
        "普通": ["红", "粉", "橙", "黄", "米", "咖", "棕"],
        "不宜": ["绿", "青", "碧"]
    },
    "水": {
        "大吉": ["绿", "青", "碧"],
        "次吉": ["蓝", "黑", "灰"],
        "普通": ["黄", "米", "咖", "棕", "金", "银", "白"],
        "不宜": ["红", "粉", "橙"]
    },
    "木": {
        "大吉": ["红", "粉", "橙"],
        "次吉": ["绿", "青", "碧"],
        "普通": ["蓝", "黑", "灰", "黄", "米", "咖", "棕"],
        "不宜": ["金", "银", "白"]
    },
    "火": {
        "大吉": ["黄", "米", "咖", "棕"],
        "次吉": ["红", "粉", "橙"],
        "普通": ["绿", "青", "碧", "蓝", "黑", "灰"],
        "不宜": ["金", "银", "白"]
    },
    "土": {
        "大吉": ["金", "银", "白"],
        "次吉": ["黄", "米", "咖", "棕"],
        "普通": ["红", "粉", "橙", "绿", "青", "碧"],
        "不宜": ["蓝", "黑", "灰"]
    }
}

# 地支对应的五行
wuxing_map = {
    "子": "水",
    "丑": "土",
    "寅": "木",
    "卯": "木",
    "辰": "土",
    "巳": "火",
    "午": "火",
    "未": "土",
    "申": "金",
    "酉": "金",
    "戌": "土",
    "亥": "水"
}

def create():
  # 创建日历对象
  calendar = Calendar()

  # 遍历2024年的每一天
  start_date = datetime.date(2024, 1, 1)
  end_date = datetime.date(2024, 12, 31)
  delta = datetime.timedelta(days=1)
  current_date = start_date

  while current_date <= end_date: 
    ganzhi = Lunar.getDayGanzhi(current_date)
    dizhi = ganzhi[1]
    # 获取五行
    wuxing_of_day = wuxing_map[dizhi]
    colors = wuxing_colors[wuxing_of_day]

    # 创建事件
    event = Event()
    event.name = f"大吉：{', '.join(colors['大吉'])}" + "," + f"不宜：{', '.join(colors['不宜'])}"
    event.begin = current_date
    # 设置事件持续时间，例如1小时
    event.duration = datetime.timedelta(hours=1)
    event.description = (
        f"大吉：{', '.join(colors['大吉'])}\n"
        f"次吉：{', '.join(colors['次吉'])}\n"
        f"不宜：{', '.join(colors['不宜'])}"
    )
    # 将事件添加到日历
    calendar.events.add(event)
    current_date += delta

  # 将日历保存为 .ics 文件
  with open('test.ics', 'w', encoding='utf-8') as f:
    f.writelines(calendar)
  print("日历文件生成成功：test.ics")  

if __name__ == '__main__':
    create()