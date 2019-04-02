from abc import abstractmethod, ABC


class ActorSpec(ABC):

    @property
    @abstractmethod
    def policy_type(self) -> str:
        pass


class CriticSpec(ABC):

    @property
    @abstractmethod
    def num_outputs(self) -> int:
        pass

    @property
    @abstractmethod
    def num_atoms(self) -> int:
        pass
