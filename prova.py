def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    result = []

    while len(result) < len(packages):
        ready = [
            pacote
            for pacote in sorted(packages)
            if pacote not in result
            and all(
                dependencia not in packages or dependencia in result
                for dependencia in packages[pacote]
            )
        ]

        if not ready:
            return []

        result.extend(ready)

    return result



print(package_dependency_resolver({
    "app": ["database"],
    "database": ["driver"],
    "driver": []
}))
# Esperado: ['driver', 'database', 'app']

print(package_dependency_resolver({"B": [], "A": []}))
# Esperado: ['A', 'B']

print(package_dependency_resolver({"A": ["B"], "B": ["A"]}))
# Esperado: []

print(package_dependency_resolver({"app": ["ausente"]}))
# Esperado: ['app']

print(package_dependency_resolver({}))
# Esperado: []