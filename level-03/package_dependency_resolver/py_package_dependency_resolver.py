def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
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

	return result




if __name__ == "__main__":
	print("Result:", package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []}), "| Expected:", ["driver", "database", "app"])
	print("Result:", package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]}), "| Expected:", ["A", "B", "C"])
	print("Result:", package_dependency_resolver({}), "| Expected:", [])
	print("Result:", package_dependency_resolver({"X": ["Y"], "Y": ["X"]}), "| Expected:", [])
	print("Result:", package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}), "| Expected:", ["api", "web", "backend", "frontend"])
