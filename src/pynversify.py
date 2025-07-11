class Container:
    def __init__(self):
        self._providers = {}

    class _Binder:
        def __init__(self, container, cls):
            self.container = container
            self.cls = cls

        def to_self(self):
            self.container._providers[self.cls] = self.cls
            return self

        def to_factory(self, factory):
            self.container._providers[self.cls] = factory
            return self

    def bind(self, cls):
        return Container._Binder(self, cls)

    def get(self, cls):
        provider = self._providers.get(cls)
        if provider is None:
            raise KeyError(f"No provider for {cls}")
        if isinstance(provider, type):
            return provider()
        return provider()
