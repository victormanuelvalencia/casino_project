# CRUD de jugadores, validaciones, carga/guardado en JSON

import json
import os
from players.player import Player
from utils.file_administration import read_json, write_json

class PlayerController:
    def __init__(self, file_path="data/players.json"):
        self.file_path = file_path
        self.players = self.load_players()

    def load_players(self):
        if not os.path.exists(self.file_path):
            return []

        data = read_json(self.file_path)
        return [Player.from_dict(p) for p in data]

    def save_players(self):
        data = [p.to_dict() for p in self.players]
        write_json(self.file_path, data)

    def create_player(self, full_name, player_id, balance):
        if self.get_player_by_id(player_id):
            raise ValueError(f"Player with ID {player_id} already exists.")

        new_player = Player(full_name, player_id, balance)
        self.players.append(new_player)
        self.save_players()
        return new_player

    def get_player_by_id(self, player_id):
        for player in self.players:
            if player.player_id == player_id:
                return player
        return None

    def update_balance(self, player_id, amount):
        player = self.get_player_by_id(player_id)
        if not player:
            raise ValueError(f"Player with ID {player_id} not found.")

        player.update_balance(amount)
        self.save_players()

    def delete_player(self, player_id):
        player = self.get_player_by_id(player_id)
        if player:
            self.players.remove(player)
            self.save_players()
            return True
        return False

    def list_players(self):
        return self.players