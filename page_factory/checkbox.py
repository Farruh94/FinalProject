import allure

from page_factory.component import Component


class CheckBox(Component):
    @property
    def type_of(self) -> str:
        return 'checkbox'

    def check(self, **kwargs) -> None:
        with allure.step(f'Check the {self.type_of} with name "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.check()

    def uncheck(self, **kwargs) -> None:
        with allure.step(f'Uncheck the {self.type_of} with name "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.uncheck()

    def is_checked(self, **kwargs) -> None:
        with allure.step(f'Check that the {self.type_of} with name "{self.name} is checked"'):
            locator = self.get_locator(**kwargs)
            locator.is_checked()
