def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    result = []

    while len(result) < len(packages):
        ready = [
            p for p in sorted(packages)
            if p not in result
            and all(d not in packages or d in result for d in packages[p])
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
