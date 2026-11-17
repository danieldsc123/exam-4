def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    result = []

    while len(result) < len(packages):
        ready = [ package for package in sorted(packages) if package not in result
            and all(dependency not in packages or dependency in result for dependency in packages[package])
        ]

        if not ready:
            return []

        result.extend(ready)

    return result



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
