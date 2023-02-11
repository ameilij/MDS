# importamos las librerias necesarias
import pandas as pd
import numpy as np
from copy import deepcopy

# Formato de los decimales en Pandas y la semilla del Random
pd.options.display.float_format = '{:,.2f}'.format
np.random.seed(5)


class Environment(object):
    def __init__(self, action_penalty=-1.0):
        """
        Clase que representa y controla en entorno
        :param step_penalty: Factor de descuento del Reward por acción tomada
        """
        self.actions = {'Arriba': [-1, 0],
                        'Abajo': [1, 0],
                        'Izquierda': [0, -1],
                        'Derecha': [0, 1]}
        self.rewards = [[0.0, 0.0, 0.0, 0.0],
                        [0.0, 0.0, 0.0, 0.0],
                        [0.0, 0.0, 0.0, 0.0],
                        [0.0, 0.0, -100.0, 100.0]]
        self.action_penalty = action_penalty
        self.state = [0, 0]
        self.final_state = [3, 3]
        self.total_reward = 0.0
        self.actions_done = []

    def reset(self):
        """
        Método que reinicia las variables del entorno y devuelve es estado inicial
        :return: state
        """
        self.total_reward = 0.0
        self.state = [0, 0]
        self.actions_done = []
        return self.state

    def step(self, action):
        """
        Método que ejecuta una acción determinada del conjunto de acciones {Arriba, Abajo, Izquierda, Derecha}
        para guiar al agente en el entorno.
        :param action: Acción a ejecutar
        :return: (state, reward, is_final_state)
        """
        self.__apply_action(action)
        self.actions_done.append(self.state[:])
        is_final_state = np.array_equal(self.state, self.final_state)
        reward = self.rewards[self.state[0]][self.state[1]] + self.action_penalty
        self.total_reward += reward
        return self.state, reward, is_final_state

    def __apply_action(self, action):
        """
        Método que calcula el nuevo estado a partir de la acción a ejecutar
        :param action: Acción a ejecutar
        """
        self.state[0] += self.actions[action][0]
        self.state[1] += self.actions[action][1]

        # Si me salgo del tablero por arriba o por abajo, me quedo en la posición que estaba
        if self.state[0] < 0:
            self.state[0] = 0
        elif self.state[0] > len(self.rewards) - 1:
            self.state[0] -= 1

        # Si me salgo del tablero por los lados, me quedo en la posición que estaba
        if self.state[1] < 0:
            self.state[1] = 0
        elif self.state[1] > len(self.rewards[0]) - 1:
            self.state[1] -= 1

    def print_path_episode(self):
        """
        Método que imprime por pantalla el camino seguido por el agente
        :return: 
        """
        path = [['-' for _ in range(len(self.rewards))] for _ in range(len(self.rewards[0]))]
        path[0][0] = '0'
        for index, step in enumerate(self.actions_done):
            path[step[0]][step[1]] = str(index + 1)

        print(pd.DataFrame(data=np.array([np.array(xi) for xi in path]),
                           index=["x{}".format(str(i)) for i in range(len(path))],
                           columns=["y{}".format(str(i)) for i in range(len(path[0]))]))

class Learner(object):

    def __init__(self, environment, learning_rate=0.1, discount_factor=0.1, ratio_exploration=0.05):
        """
        Clase que implementa un algoritmo de aprendizaje por refuerzo
        Esta clase implementa un algoritmo de selección aleatoria de acciones
        :param environment: Entorno en el que tomar las acciones
        :param learning_rate: Factor de aprendizaje
        :param discount_factor: Factor de descuento (0=Estrategia a corto plazo, 1=Estrategia a largo plazo)
        :param ratio_exploration: Ratio de exploración
        """
        self.environment = environment
        self.q_table = [[[0.0 for _ in self.environment.actions]
                         for _ in range(len(self.environment.rewards))]
                        for _ in range(len(self.environment.rewards[0]))]
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.ratio_exploration = ratio_exploration

    @property
    def name(self):
        return 'random'

    def get_next_action(self, state):
        """
        Método que selecciona la siguiente acción a tomar:
            Aleatoria -> si el ratio de exploración es inferior al umbral
            Mejor Acción -> si el ratio de exploración es superior al umbral
        :param state: Estado del agente
        :return: next_action
        """

        if np.random.uniform() < self.ratio_exploration:
            # Selecciono una opción al azar
            next_action = np.random.choice(list(self.environment.actions))
        else:
            # Selecciono la acción que me de mayor valor. Si hay empate, selecciono una al azar
            idx_action = np.random.choice(np.flatnonzero(
                self.q_table[state[0]][state[1]] == np.array(self.q_table[state[0]][state[1]]).max()
            ))
            next_action = list(self.environment.actions)[idx_action]

        return next_action

    def update(self, **kwargs):
        """
        Actualiza la Q-Table
        :param kwargs: 
        """
        pass

    def print_q_table(self):
        """
        Método que imprime por pantalla la Q-Table
        """
        print("Actions = {}".format(' - '.join([k for k, v in self.environment.actions.items()])))
        for row in self.q_table:
            for col in row:
                print('[', end='')
                for val in col:
                    print('{:0.2f}'.format(val), end=' ')
                print('] ', end='')
            print()

    def print_best_values_states(self):
        """
        Método que imprime por pantalla el valor de la mejor opción a realizar en cada uno de los estados
        """
        best = [[max(vi) for vi in row] for row in self.q_table]
        print(pd.DataFrame(data=np.array([np.array(xi) for xi in best]),
                           index=["x{}".format(str(i)) for i in range(len(best))],
                           columns=["y{}".format(str(i)) for i in range(len(best[0]))]))

def run_agent(learner=Learner, num_episodes=10, learning_rate=0.1, discount_factor=0.1, ratio_exploration=0.05,
              verbose=False):
    """
    Método que ejecuta el proceso de aprendizaje del agente en un entorno
    :param learner: Algoritmo de Aprendizaje
    :param num_episodes: Número de veces que se ejecuta (o aprende) el agente en el entorno
    :param learning_rate: Factor de Aprendizaje
    :param discount_factor: Factor de descuento (0=Estrategia a corto plazo, 1=Estrategia a largo plazo)
    :param ratio_exploration: Ratio de exploración
    :param verbose: Boolean, si queremos o no imprimir por pantalla información del proceso
    :return: (episodes_list, best_episode)
    """

    # Instanciamos el entorno
    environment = Environment()

    # Instanciamos el método de aprendizaje
    learner = learner(environment=environment,
                      learning_rate=learning_rate,
                      discount_factor=discount_factor,
                      ratio_exploration=ratio_exploration)

    # Variables para guardar la información de los episodios
    episodes_list = []
    best_reward = float('-inf')
    best_episode = None

    for n_episode in range(0, num_episodes):
        state = environment.reset()
        reward = None
        is_final_state = None
        num_steps_episode = 0
        while (is_final_state != True):
            old_state = state[:]
            next_action = learner.get_next_action(state=state)
            state, reward, is_final_state = environment.step(next_action)
            next_post_action = learner.get_next_action(state) if learner.name == 'SARSA' else None
            learner.update(environment=environment,
                           old_state=old_state,
                           action_taken=next_action,
                           reward_action_taken=reward,
                           new_state=state,
                           new_action=next_post_action,
                           is_final_state=is_final_state)
            num_steps_episode += 1

        # Guardamos la información del episodio
        episodes_list.append([n_episode + 1, num_steps_episode, environment.total_reward])

        # Guardamos el mejor episodio
        if environment.total_reward >= best_reward:
            best_reward = environment.total_reward
            best_episode = {'num_episode': n_episode + 1,
                            'episode': deepcopy(environment),
                            'learner': deepcopy(learner)}

        if verbose:
            # Imprimimos la información de los episodios
            print('EPISODIO {} - Numero de acciones: {} - Reward: {}'
                  .format(n_episode + 1, num_steps_episode, environment.total_reward))

    return episodes_list, best_episode


def print_process_info(episodes_list, best_episode, print_best_episode_info=True,
                       print_q_table=True, print_best_values_states=True,
                       print_steps=True, print_path=True):
    """
    Método que imprime por pantalla los resultados de la ejecución
    """
    if print_best_episode_info:
        print('\nMEJOR (ÚLTIMO) EPISODIO:\n\EPISODIO {}\n\tNumero de acciones: {}\n\tReward: {}'
              .format(best_episode['num_episode'],
                      len(best_episode['episode'].actions_done),
                      best_episode['episode'].total_reward))

    if print_q_table:
        print('\nQ_TABLE:')
        best_episode['learner'].print_q_table()

    if print_best_values_states:
        print('\nBEST Q_TABLE VALUES:')
        best_episode['learner'].print_best_values_states()

    if print_steps:
        print('\nPasos: \n   {}'.format(best_episode['episode'].actions_done))

    if print_path:
        print('\nPATH:')
        best_episode['episode'].print_path_episode()
