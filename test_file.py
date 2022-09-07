n_best_size = 1
max_answer_length = 30
do_lower_case = True
null_score_diff_threshold = 0.0


def to_list(tensor):
    return tensor.detach().cpu().tolist()