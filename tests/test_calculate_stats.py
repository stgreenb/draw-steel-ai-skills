"""Test suite for Draw Steel Monster Generator."""

import pytest
from math import ceil

from scripts.calculate_stats import (
    calculate_all_stats,
    calculate_damage,
    calculate_ev,
    calculate_free_strike,
    calculate_stamina,
    Organization,
    Role,
    TIER_MULTIPLIERS,
)


class TestOrganization:
    """Test Organization enum and conversions."""

    def test_organization_values(self):
        """Test all organization values are correct."""
        assert Organization.MINION.ev_modifier == 0.5
        assert Organization.MINION.stamina_modifier == 0.5
        assert Organization.MINION.damage_division is True

        assert Organization.HORDE.ev_modifier == 0.5
        assert Organization.HORDE.damage_division is True

        assert Organization.PLATOON.ev_modifier == 1.0
        assert Organization.PLATOON.damage_division is False

        assert Organization.ELITE.ev_modifier == 2.0
        assert Organization.ELITE.damage_modifier == 2.0

        assert Organization.LEADER.ev_modifier == 2.0
        assert Organization.SOLO.ev_modifier == 6.0
        assert Organization.SOLO.damage_modifier == 6.0

    def test_organization_from_string(self):
        """Test converting string to Organization enum."""
        assert Organization.from_string("Platoon") == Organization.PLATOON
        assert Organization.from_string("platoon") == Organization.PLATOON
        assert Organization.from_string("SOLO") == Organization.SOLO

    def test_organization_invalid(self):
        """Test invalid organization raises ValueError."""
        with pytest.raises(ValueError) as exc_info:
            Organization.from_string("InvalidOrg")
        assert "Unknown organization" in str(exc_info.value)


class TestRole:
    """Test Role enum and conversions."""

    def test_role_values(self):
        """Test all role values are correct."""
        assert Role.AMBUSHER.stamina_modifier == 20
        assert Role.AMBUSHER.damage_modifier == 1

        assert Role.BRUTE.stamina_modifier == 30
        assert Role.BRUTE.damage_modifier == 1

        assert Role.HARRIER.stamina_modifier == 20
        assert Role.HARRIER.damage_modifier == 0

        assert Role.CONTROLLER.stamina_modifier == 10
        assert Role.CONTROLLER.damage_modifier == 0

    def test_role_from_string(self):
        """Test converting string to Role enum."""
        assert Role.from_string("Harrier") == Role.HARRIER
        assert Role.from_string("harrier") == Role.HARRIER
        assert Role.from_string("BRUTE") == Role.BRUTE

    def test_role_invalid(self):
        """Test invalid role raises ValueError."""
        with pytest.raises(ValueError) as exc_info:
            Role.from_string("InvalidRole")
        assert "Unknown role" in str(exc_info.value)


class TestCalculateEV:
    """Test EV calculation."""

    @pytest.mark.parametrize("org", Organization)
    def test_ev_formula_all_orgs(self, org):
        """Test EV formula for all organizations."""
        for level in range(1, 11):
            ev = calculate_ev(level, org)
            expected = ceil(((2 * level) + 4) * org.ev_modifier)
            assert ev == expected, f"EV mismatch for Level {level} {org}"

    def test_ev_level_1_platoon(self):
        """Test Level 1 Platoon EV."""
        ev = calculate_ev(1, Organization.PLATOON)
        assert ev == ceil(((2 * 1) + 4) * 1.0)

    def test_ev_level_10_solo(self):
        """Test Level 10 Solo EV."""
        ev = calculate_ev(10, Organization.SOLO)
        assert ev == ceil(((2 * 10) + 4) * 6.0)

    def test_ev_invalid_level_too_low(self):
        """Test invalid level (too low) raises ValueError."""
        with pytest.raises(ValueError):
            calculate_ev(0, Organization.PLATOON)

    def test_ev_invalid_level_too_high(self):
        """Test invalid level (too high) raises ValueError."""
        with pytest.raises(ValueError):
            calculate_ev(11, Organization.PLATOON)


class TestCalculateStamina:
    """Test Stamina calculation."""

    @pytest.mark.parametrize("role", Role)
    def test_stamina_formula_all_roles(self, role):
        """Test Stamina formula for all roles."""
        org = Organization.PLATOON
        for level in range(1, 11):
            stamina = calculate_stamina(level, role, org)
            expected = ceil(
                ((10 * level) + role.stamina_modifier) * org.stamina_modifier
            )
            assert stamina == expected

    def test_stamina_harrier_platoon_l3(self):
        """Test Level 3 Platoon Harrier Stamina."""
        stamina = calculate_stamina(3, Role.HARRIER, Organization.PLATOON)
        expected = ceil(((10 * 3) + 20) * 1.0)
        assert stamina == expected == 50

    def test_stamina_brute_solo_l5(self):
        """Test Level 5 Solo Brute Stamina."""
        stamina = calculate_stamina(5, Role.BRUTE, Organization.SOLO)
        expected = ceil(((10 * 5) + 30) * 6.0)
        assert stamina == expected == 480


class TestCalculateDamage:
    """Test Damage calculation."""

    def test_tier_multipliers(self):
        """Test tier multipliers are correct."""
        assert TIER_MULTIPLIERS[1] == 0.6
        assert TIER_MULTIPLIERS[2] == 1.1
        assert TIER_MULTIPLIERS[3] == 1.4

    @pytest.mark.parametrize("tier", [1, 2, 3])
    def test_damage_tiers(self, tier):
        """Test damage calculation for all tiers."""
        org = Organization.PLATOON
        role = Role.HARRIER
        level = 3
        damage = calculate_damage(level, role, tier, org)
        base = 4 + level + role.damage_modifier
        expected = ceil(base * TIER_MULTIPLIERS[tier])
        assert damage == expected

    def test_damage_horde_divided_by_2(self):
        """Test Horde damage is divided by 2."""
        org = Organization.HORDE
        role = Role.CONTROLLER
        level = 3

        damage_t1 = calculate_damage(level, role, 1, org)
        base = 4 + level + role.damage_modifier
        expected = ceil(ceil(base * 0.6) / 2)
        assert damage_t1 == expected

    def test_damage_minion_divided_by_2(self):
        """Test Minion damage is divided by 2."""
        org = Organization.MINION
        role = Role.AMBUSHER
        level = 1

        damage_t1 = calculate_damage(level, role, 1, org)
        base = 4 + level + role.damage_modifier
        expected = ceil(ceil(base * 0.6) / 2)
        assert damage_t1 == expected

    def test_damage_solo_multiplied(self):
        """Test Solo damage is multiplied."""
        org = Organization.SOLO
        role = Role.BRUTE
        level = 5

        damage_t1 = calculate_damage(level, role, 1, org)
        base = 4 + level + role.damage_modifier
        expected = ceil(base * 0.6 * 6.0)
        assert damage_t1 == expected

    def test_damage_invalid_tier(self):
        """Test invalid tier raises ValueError."""
        with pytest.raises(ValueError):
            calculate_damage(3, Role.HARRIER, 4, Organization.PLATOON)


class TestCalculateFreeStrike:
    """Test Free Strike calculation."""

    def test_free_strike_equals_t1_damage(self):
        """Test Free Strike equals Tier 1 damage."""
        level = 3
        role = Role.HARRIER
        org = Organization.PLATOON

        free_strike = calculate_free_strike(level, role, org)
        damage_t1 = calculate_damage(level, role, 1, org)

        assert free_strike == damage_t1

    def test_free_strike_horde(self):
        """Test Free Strike for Horde creature."""
        level = 1
        role = Role.AMBUSHER
        org = Organization.HORDE

        free_strike = calculate_free_strike(level, role, org)
        damage_t1 = calculate_damage(level, role, 1, org)

        assert free_strike == damage_t1


class TestCalculateAllStats:
    """Test calculate_all_stats integration function."""

    def test_all_stats_l3_platoon_harrier(self):
        """Test Level 3 Platoon Harrier."""
        result = calculate_all_stats(3, Organization.PLATOON, Role.HARRIER)

        assert result["level"] == 3
        assert result["organization"] == "Platoon"
        assert result["role"] == "Harrier"
        assert result["ev"] == 10
        assert result["stamina"] == 50
        assert result["free_strike"] == 5
        assert result["damage_t1"] == 5
        assert result["damage_t2"] == 8
        assert result["damage_t3"] == 10
        assert result["error"] is None

    def test_all_stats_l5_solo_brute(self):
        """Test Level 5 Solo Brute."""
        result = calculate_all_stats(5, Organization.SOLO, Role.BRUTE)

        assert result["level"] == 5
        assert result["organization"] == "Solo"
        assert result["role"] == "Brute"
        assert result["ev"] == 84
        assert result["stamina"] == 480
        assert result["free_strike"] == 36
        assert result["damage_t1"] == 36
        assert result["damage_t2"] == 66
        assert result["damage_t3"] == 84

    def test_all_stats_from_strings(self):
        """Test calculate_all_stats with string inputs."""
        result = calculate_all_stats(3, "Platoon", "Harrier")

        assert result["organization"] == "Platoon"
        assert result["role"] == "Harrier"

    def test_all_stats_l1_horde_ambusher(self):
        """Test Level 1 Horde Ambusher."""
        result = calculate_all_stats(1, Organization.HORDE, Role.AMBUSHER)

        assert result["level"] == 1
        assert result["organization"] == "Horde"
        assert result["role"] == "Ambusher"
        assert result["ev"] == 3
        assert result["stamina"] == 15
        assert result["free_strike"] == 2
        assert result["damage_t1"] == 2
        assert result["damage_t2"] == 4
        assert result["damage_t3"] == 5

    def test_all_stats_l4_elite_defender(self):
        """Test Level 4 Elite Defender."""
        result = calculate_all_stats(4, Organization.ELITE, Role.DEFENDER)

        assert result["ev"] == 24
        assert result["stamina"] == 140
        assert result["free_strike"] == 10
        assert result["damage_t1"] == 10
        assert result["damage_t2"] == 18
        assert result["damage_t3"] == 24

    def test_all_stats_l2_platoon_hexer(self):
        """Test Level 2 Platoon Hexer."""
        result = calculate_all_stats(2, Organization.PLATOON, Role.HEXER)

        assert result["ev"] == 8
        assert result["stamina"] == 30
        assert result["free_strike"] == 4
        assert result["damage_t1"] == 4
        assert result["damage_t2"] == 7
        assert result["damage_t3"] == 9


class TestExampleCreatures:
    """Test examples from examples.md match calculated values."""

    @pytest.fixture
    def griffin_stats(self):
        """Return Griffin (Level 3, Platoon, Harrier) expected values."""
        return {
            "ev": 10,
            "stamina": 50,
            "free_strike": 5,
            "damage_t1": 5,
            "damage_t2": 8,
            "damage_t3": 10,
        }

    @pytest.fixture
    def dragon_stats(self):
        """Return Red Dragon (Level 5, Solo, Brute) expected values."""
        return {
            "ev": 84,
            "stamina": 480,
            "free_strike": 36,
            "damage_t1": 36,
            "damage_t2": 66,
            "damage_t3": 84,
        }

    @pytest.fixture
    def goblin_stats(self):
        """Return Goblin Scout (Level 1, Horde, Ambusher) expected values."""
        return {
            "ev": 3,
            "stamina": 15,
            "free_strike": 2,
            "damage_t1": 2,
            "damage_t2": 4,
            "damage_t3": 5,
        }

    @pytest.fixture
    def golem_stats(self):
        """Return Stone Golem (Level 4, Elite, Defender) expected values."""
        return {
            "ev": 24,
            "stamina": 140,
            "free_strike": 10,
            "damage_t1": 10,
            "damage_t2": 18,
            "damage_t3": 24,
        }

    @pytest.fixture
    def wisp_stats(self):
        """Return Will-o'-Wisp (Level 2, Platoon, Hexer) expected values."""
        return {
            "ev": 8,
            "stamina": 30,
            "free_strike": 4,
            "damage_t1": 4,
            "damage_t2": 7,
            "damage_t3": 9,
        }

    def test_griffin(self, griffin_stats):
        """Test Griffin matches expected values."""
        result = calculate_all_stats(3, Organization.PLATOON, Role.HARRIER)
        assert result["ev"] == griffin_stats["ev"]
        assert result["stamina"] == griffin_stats["stamina"]
        assert result["free_strike"] == griffin_stats["free_strike"]
        assert result["damage_t1"] == griffin_stats["damage_t1"]
        assert result["damage_t2"] == griffin_stats["damage_t2"]
        assert result["damage_t3"] == griffin_stats["damage_t3"]

    def test_dragon(self, dragon_stats):
        """Test Red Dragon matches expected values."""
        result = calculate_all_stats(5, Organization.SOLO, Role.BRUTE)
        assert result["ev"] == dragon_stats["ev"]
        assert result["stamina"] == dragon_stats["stamina"]
        assert result["free_strike"] == dragon_stats["free_strike"]
        assert result["damage_t1"] == dragon_stats["damage_t1"]
        assert result["damage_t2"] == dragon_stats["damage_t2"]
        assert result["damage_t3"] == dragon_stats["damage_t3"]

    def test_goblin(self, goblin_stats):
        """Test Goblin Scout matches expected values."""
        result = calculate_all_stats(1, Organization.HORDE, Role.AMBUSHER)
        assert result["ev"] == goblin_stats["ev"]
        assert result["stamina"] == goblin_stats["stamina"]
        assert result["free_strike"] == goblin_stats["free_strike"]
        assert result["damage_t1"] == goblin_stats["damage_t1"]
        assert result["damage_t2"] == goblin_stats["damage_t2"]
        assert result["damage_t3"] == goblin_stats["damage_t3"]

    def test_golem(self, golem_stats):
        """Test Stone Golem matches expected values."""
        result = calculate_all_stats(4, Organization.ELITE, Role.DEFENDER)
        assert result["ev"] == golem_stats["ev"]
        assert result["stamina"] == golem_stats["stamina"]
        assert result["free_strike"] == golem_stats["free_strike"]
        assert result["damage_t1"] == golem_stats["damage_t1"]
        assert result["damage_t2"] == golem_stats["damage_t2"]
        assert result["damage_t3"] == golem_stats["damage_t3"]

    def test_wisp(self, wisp_stats):
        """Test Will-o'-Wisp matches expected values."""
        result = calculate_all_stats(2, Organization.PLATOON, Role.HEXER)
        assert result["ev"] == wisp_stats["ev"]
        assert result["stamina"] == wisp_stats["stamina"]
        assert result["free_strike"] == wisp_stats["free_strike"]
        assert result["damage_t1"] == wisp_stats["damage_t1"]
        assert result["damage_t2"] == wisp_stats["damage_t2"]
        assert result["damage_t3"] == wisp_stats["damage_t3"]
