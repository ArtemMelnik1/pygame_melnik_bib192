import os
import sys

from solution.static.static_data import StaticData


class AbsolutePath:
    @staticmethod
    def routine():
        """
        Функция для генерации абсолютных путей для статических файлов.
        """
        for address, dirs, files in os.walk(StaticData.items_path):
            for file in files:
                if sys.platform != 'win32':
                    StaticData.absolute_paths.update(
                        {file: str(os.path.abspath('') + '/items/' + file).replace('/solution', '').replace('/moving',
                                                                                                            '')})
                else:
                    StaticData.absolute_paths.update(
                        {file: str(os.path.abspath('') + '\\items\\' + file).replace('\\solution', '').replace(
                            '\\moving',
                            '')})

        print(StaticData.absolute_paths)
