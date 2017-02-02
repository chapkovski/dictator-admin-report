from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random
from otree.common import safe_json

class Introduction(Page):
    pass


class Offer(Page):

    form_model = models.Player
    form_fields = ['kept']
    def vars_for_template(self):
        pass
        # numLow = 0
        # numHigh = 10
        # n = 10
        # listOfNumbers = []
        # for p in self.player.in_all_rounds():
        #     if p.kept is not None:
        #         listOfNumbers.append(int(p.kept))
        # toadd = ['']*(Constants.num_rounds-len(listOfNumbers))
        # listOfNumbers += toadd
        # round_numbers = safe_json(list(range(1, Constants.num_rounds+1)))
        # # print("LIST OF rounds: {}".format(round_numbers))
        # myseries = []
        # myseries.append({
        # 'name': 'decisions',
        # 'data': listOfNumbers})
        # series_to_pass = safe_json(myseries)
        # # print("jsonied series: {} =============".format(series_to_pass))
        # return {
        #     'series_to_pass':series_to_pass,
        #     'round_numbers':round_numbers,
        # }
    # def is_displayed(self):
    #     return self.player.id_in_group == 1


# class ResultsWaitPage(WaitPage):
#     def after_all_players_arrive(self):
#         self.group.set_payoffs()
#
#     def vars_for_template(self):
#         if self.player.id_in_group == 2:
#             body_text = "You are participant 2. Waiting for participant 1 to decide."
#         else:
#             body_text = 'Please wait'
#         return {'body_text': body_text}
class MyPage(Page):
    form_model = models.Player
    template_name = 'dictatorMU/Offer.html'
    title = ''
    instructions = ''
    def vars_for_template(self):
        vs = {
            'title': self.title,
            'instructions': self.instructions,
        }
        vs.update(self.extra_vars())
        return vs

    def extra_vars(self):
        return {}

class Kept(MyPage):
    form_fields = ['kept']
    title = 'Decision'
    instructions = 'dictatorMU/InstructionsDecision.html'

class Belief(MyPage):
    form_fields = ['belief']
    title = 'Belief'
    instructions = 'dictatorMU/InstructionsBelief.html'

class Norm(MyPage):
    form_fields = ['norm']
    title = 'Norm'
    instructions = ''

class Others_belief(MyPage):
    form_fields = ['others_belief']
    title = "Others' beliefs"
    instructions = 'dictatorMU/InstructionsOtherBelief.html'

class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    def offer(self):
        return Constants.endowment - self.player.kept

    def vars_for_template(self):
        print('PLAYER KEPT: {}'.format(self.player.kept))
        all_decisions = [random.randint(0,Constants.endowment) for r in range(25)]
        all_beliefs = [random.randint(0,Constants.endowment) for r in range(25)]
        all_norms = [random.randint(0,Constants.endowment) for r in range(25)]
        all_others_beliefs = [random.randint(0,Constants.endowment) for r in range(25)]

        return {
            'all_decisions':safe_json(all_decisions),
            'all_beliefs':safe_json(all_beliefs),
            'all_norms':safe_json(all_norms),
            'all_others_beliefs':safe_json(all_others_beliefs),
            'average_decision':sum(all_decisions)/len(all_decisions),
            'average_belief':sum(all_beliefs)/len(all_beliefs),
            'average_norm':sum(all_norms)/len(all_norms),
            'average_others_belief':sum(all_others_beliefs)/len(all_others_beliefs),
        }


page_sequence = [
    Kept,
    Belief,
    Norm,
    Others_belief,
    # ResultsWaitPage,
    Results
]
