#! /usr/bin/env python

"""
   Program:   EQ Alert
   File Name: eqa/lib/state.py
   Copyright (C) 2023 M Geitz

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2 of the License, or
   (at your option) any later version.
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   You should have received a copy of the GNU General Public License along
   with this program; if not, write to the Free Software Foundation, Inc.,
   51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

   Parse and react to eqemu logs
"""


class EQA_State:
    """Track State"""

    def __init__(
        self,
        char,
        chars,
        zone,
        loc,
        direction,
        afk,
        server,
        raid,
        debug,
        mute,
        group,
        leader,
        encumbered,
        bind,
        char_level,
        char_class,
        char_guild,
        encounter_parse,
        save_parse,
        auto_raid,
        auto_mob_timer,
        auto_mob_timer_delay,
        consider_eval,
        detect_char,
        spell_timer_delay,
        spell_timer_guess,
        spell_timer_other,
        spell_timer_guild_only,
        spell_timer_self,
        spell_timer_yours_only,
    ):
        """All States"""
        self.char = char
        self.chars = chars
        self.zone = zone
        self.loc = loc
        self.direction = direction
        self.afk = afk
        self.server = server
        self.raid = raid
        self.debug = debug
        self.mute = mute
        self.group = group
        self.leader = leader
        self.encumbered = encumbered
        self.bind = bind
        self.char_level = char_level
        self.char_class = char_class
        self.char_guild = char_guild
        self.encounter_parse = encounter_parse
        self.save_parse = save_parse
        self.auto_raid = auto_raid
        self.auto_mob_timer = auto_mob_timer
        self.auto_mob_timer_delay = auto_mob_timer_delay
        self.consider_eval = consider_eval
        self.detect_char = detect_char
        self.spell_timer_delay = spell_timer_delay
        self.spell_timer_guess = spell_timer_guess
        self.spell_timer_other = spell_timer_other
        self.spell_timer_guild_only = spell_timer_guild_only
        self.spell_timer_self = spell_timer_self
        self.spell_timer_yours_only = spell_timer_yours_only

    def set_char(self, char):
        """Set Character"""
        self.char = char

    def set_chars(self, chars):
        """Set Characters"""
        self.chars = chars

    def set_zone(self, zone):
        """Set Zone"""
        self.zone = zone

    def set_loc(self, loc):
        """Set Location"""
        self.loc = loc

    def set_direction(self, direction):
        """Set Direction"""
        self.direction = direction

    def set_afk(self, afk):
        """Set AFK"""
        self.afk = afk

    def set_server(self, server):
        """Set Server"""
        self.server = server

    def set_raid(self, raid):
        """Set Raid"""
        self.raid = raid

    def set_debug(self, debug):
        """Set Debug"""
        self.debug = debug

    def set_mute(self, mute):
        """Set Mute"""
        self.mute = mute

    def set_group(self, group):
        """Set Group"""
        self.group = group

    def set_leader(self, leader):
        """Set Leader"""
        self.leader = leader

    def set_encumbered(self, encumbered):
        """Set Encumbered"""
        self.encumbered = encumbered

    def set_bind(self, bind):
        """Set Bind"""
        self.bind = bind

    def set_level(self, char_level):
        """Set Level"""
        self.char_level = char_level

    def set_class(self, char_class):
        """Set Class"""
        self.char_class = char_class

    def set_guild(self, char_guild):
        """Set Guild"""
        self.char_guild = char_guild

    def set_encounter_parse(self, encounter_parse):
        """Set Encounter Parse"""
        self.encounter_parse = encounter_parse

    def set_encounter_parse_save(self, save_parse):
        """Set Encounter Parse Auto-Save"""
        self.save_parse = save_parse

    def set_auto_raid(self, auto_raid):
        """Toggle Automatic Raid Mode"""
        self.auto_raid = auto_raid

    def set_auto_mob_timer(self, auto_mob_timer):
        """Toggle Automatic Mob Timers"""
        self.auto_mob_timer = auto_mob_timer

    def set_auto_mob_timer_delay(self, auto_mob_timer_delay):
        """Toggle Automatic Mob Timers"""
        self.auto_mob_timer_delay = auto_mob_timer_delay

    def set_consider_eval(self, consider_eval):
        """Toggle Consider Evaluation"""
        self.consider_eval = consider_eval

    def set_detect_char(self, detect_char):
        """Toggle Automatic Character Detection"""
        self.detect_char = detect_char

    def set_spell_timer_delay(self, spell_timer_delay):
        """Set Spell Timer Delay"""
        self.spell_timer_delay = spell_timer_delay

    def set_spell_timer_guess(self, spell_timer_guess):
        """Set Spell Timer Guess"""
        self.spell_timer_guess = spell_timer_guess

    def set_spell_timer_other(self, spell_timer_other):
        """Set Spell Timer Other"""
        self.spell_timer_other = spell_timer_other

    def set_spell_timer_guild_only(self, spell_timer_guild_only):
        """Set Spell Timer Guild Only"""
        self.spell_timer_guild_only = spell_timer_guild_only

    def set_spell_timer_self(self, spell_timer_self):
        """Set Spell Timer Self"""
        self.spell_timer_self = spell_timer_self

    def set_spell_timer_yours_only(self, spell_timer_yours_only):
        """Set Spell Timer Yours Only"""
        self.spell_timer_yours_only = spell_timer_yours_only


if __name__ == "__main__":
    print("Test Here")
