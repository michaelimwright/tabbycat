import logging

from django.test import TestCase

from utils.tests import ConditionalTournamentViewLoadTest, suppress_logs


class PublicDiversityViewTest(ConditionalTournamentViewLoadTest, TestCase):
    view_name = 'standings-public-diversity'
    view_toggle = 'public_features__public_diversity'


class PublicTeamStandingsViewTest(ConditionalTournamentViewLoadTest, TestCase):
    view_name = 'standings-public-teams-current'
    view_toggle = 'public_features__public_team_standings'


class PublicRepliesTabViewTest(ConditionalTournamentViewLoadTest, TestCase):
    view_name = 'standings-public-tab-replies'
    view_toggle = 'tab_release__replies_tab_released'

    def test_set_preference(self):
        with suppress_logs('standings.metrics', logging.INFO):
            super().test_set_preference()

    def test_unset_preference(self):
        with suppress_logs('standings.metrics', logging.INFO):
            super().test_unset_preference()
