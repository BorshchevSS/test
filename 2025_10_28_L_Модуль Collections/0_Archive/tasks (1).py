# # 2
#
# from collections import defaultdict
#
# def group_products_by_category(items):
#     grouped_products = defaultdict(list)
#
#     for category, products in items:
#         grouped_products[category].append(products)
#
#     return grouped_products
#
# shopping_list = [
#     ('фрукты', 'яблоко'),
#     ('молочное', 'молоко'),
#     ('овощи', 'помидор'),
#     ('фрукты', 'виноград'),
#     ('фрукты', 'банан'),
#     ('молочное', 'сыр'),
# ]
# for item in shopping_list:
#     print(item)
# result = group_products_by_category(shopping_list)
# # print(result)
# for category, products in result.items():
#     print(f'Категория: {category}')
#     print(f'----Продукты: {', '.join(products)}')

#3
from collections import deque, Counter, defaultdict

class GameSessionAnalyzer:
    def __init__(self, window_size=100, sus_kill_thr=5):
        self.window_size = window_size
        self.event_history = deque(maxlen=window_size)
        self.active_players = set() #player_id
        self.kill_death_stats = defaultdict(lambda: Counter())
        self.sus_kill_stats =  sus_kill_thr
        self.sus_kill = defaultdict(int)

    def process_events(self, event):
        event_type, player_id, _, additional_date = event
        self.event_history.append(event)

        if event_type == 'login':
            self.active_players.add(player_id)
        elif event_type == 'logout':
            self.active_players.discard(player_id)

        if event_type == 'kill':
            enemy_id = additional_date

            self.kill_death_stats[player_id]['kills'] += 1

            pair = (player_id, enemy_id)
            self.sus_kill[pair] += 1

        elif event_type == 'death':
            killer_id = additional_date
            self.kill_death_stats[player_id]['deaths'] += 1

    def get_active_players(self):
        return list(self.active_players)


    def get_player_state(self, player_id):
        stats = self.kill_death_stats[player_id]
        return dict(stats)

    def get_sus_pairs(self):
        sus_list = []
        for (killer, victim), count in self.sus_kill.items():
            if count >= self.sus_kill_stats:
                sus_list.append((killer, victim, count))
        return sus_list

    def get_popular_items(self, top_n=5):
        item_counter = Counter()
        for event_type, _, _, additional_date in self.event_history:
            if event_type == 'collect_item':
                item_id = additional_date
                item_counter[item_id] += 1

        return item_counter.most_common(top_n)

def main():
    analyzer = GameSessionAnalyzer(window_size=100, sus_kill_thr=2)
    test_events = [
        ('login', 'P1', 100, None),
        ('login', 'P2', 101, None),
        ('collect_item', 'P1', 105, 'test1'), # + 1 test
        ('kill', 'P1', 110, 'P2'), # p1 kill p2
        ('death', 'P1', 110, 'P1'),
        ('kill', 'P1', 120, 'P2'), # pf kill p2 -> подозрение
        ('death', 'P2', 120, 'P1'),
        ('collect_item', 'P2', 125, 'test2'), # +1 test2
        ('collect_item', 'P1', 130, 'test1'), # +2 test1
        ('logout', 'P1', 140, None),
        #11 событие, первое удалится
        ('collect_item', 'P3', 150, 'test2') # +2 test2
    ]

    print("========ОБРАБОТКА СОБЫТИЙ==========")
    for event in test_events:
        analyzer.process_events(event)

    print(f'Активные игроки: {analyzer.get_active_players()}')
    print(f'Статистика Р1: {analyzer.get_player_state('P1')}')
    print(f'Статистика Р2: {analyzer.get_player_state('P2')}')
    print(f'Подозрительные пары: {analyzer.get_sus_pairs()}')
    print(f'Популярные предметы: {analyzer.get_popular_items(top_n=2)}')


