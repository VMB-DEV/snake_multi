
class LeaderBoard:
    file_name = "leader_board.txt"

    def __init__(self):
        file = open(self.file_name, 'a+')  # create file if it does not exist
        file.close()

    @classmethod
    def get_scores(cls):
        file = open(cls.file_name, 'r')
        lines = file.read().split('\n')[:-1]
        scores = {}
        for line in lines:
            split = line.split()
            scores[split[0]] = split[1]
        scores = LeaderBoard.reorder(scores)
        LeaderBoard.write_scores(scores)
        file.close()
        return scores

    @classmethod
    def write_scores(cls, scores):
        file = open(cls.file_name, 'w')
        str = ""
        for point in scores.keys():
            str += f"{point} {scores[point]}\n"
        file.write(str)

    @classmethod
    def save_score_and_name(cls, name, score):
        file = open(LeaderBoard.file_name, 'a')
        file.write(f"{score} {name}\n")
        file.close()

    @classmethod
    def reorder(cls, scores):
        sorted_dict_num = dict(sorted(scores.items(), key=lambda x: int(x[0]), reverse=True))
        return sorted_dict_num