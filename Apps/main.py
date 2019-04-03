from Apps.Daily.daily import DailyQ
# Response should be written in this function
from Apps import aiml_local, aiml
# import Apps.vector_similarity as v_sim


def response(Question):
    # BEGIN: cj_block

    # END

    # BEGIN: Allen_block
    # QAPair = v_sim.respond(Question, topn=3)
    # if QAPair and QAPair[0].sim > 0.9:
    #     Answer = "你是想问%s吗? (查看到相似度为%.4f)\n%s" % (QAPair[0].Q, QAPair[0].sim, QAPair[0].A)
    #     return Answer
    # END

    # BEGIN: tropping_block
    Answer = DailyQ(Question, "test")
    return Answer
    # END
