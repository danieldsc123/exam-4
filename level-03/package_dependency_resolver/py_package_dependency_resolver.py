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

    return sorted(result)




"""def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
	result = []
	pending = {}

	for package, dependencies in packages.items():
		pending[package] = set()

		for dependency in dependencies:
			if dependency in packages:
				pending[package].add(dependency)

	while pending:
		ready = []

		for package in sorted(pending):
			if not pending[package]:
				ready.append(package)

		if not ready:
			return []

		for package in ready:
			result.append(package)
			del pending[package]

		for dependencies in pending.values():
			dependencies.difference_update(ready)

	return result"""
