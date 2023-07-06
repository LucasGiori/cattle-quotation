from typing import Union, Type, Any
import inspect

class Container:
    def __init__(self):
        self.dependencies = {}

    def register(self, key: Union[str, Type], dependency: Type) -> None:
        key = self._make_key(key=key)
        
        self.dependencies[key] = self._create_lazy_dependency(dependency)

    def _create_lazy_dependency(self, dependency):
        def lazy_loader():
            if callable(dependency):
                return dependency()
            return dependency

        return lazy_loader

    def get(self, key: Union[str, Type]) -> Any:
        key = self._make_key(key=key)
        
        if key not in self.dependencies:
            raise KeyError(f"Dependency '{key}' is not registered.")

        dependency = self.dependencies[key]
        if callable(dependency):
            dependency = self._resolve_dependency(dependency=dependency)
            self._save_to_cache(key=key, dependency=dependency)

        return dependency
    
    def _resolve_dependency(self, dependency: callable) -> Any:
        return dependency()

    def _save_to_cache(self, key: str, dependency: Any) -> None:
        self.dependencies[key] = dependency

    
    def _make_key(self, key: Union[str, Type]) -> str:
        return key.__name__ if inspect.isclass(object=key) else key