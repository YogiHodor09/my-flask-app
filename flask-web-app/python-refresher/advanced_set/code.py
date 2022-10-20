local = {'Yogeshwar', 'Danush', 'Prathyu'}
abroad = {'Danush', 'Uma', 'Yogeshwar'}

local_friends = local.difference(abroad)

print(local_friends)

friends = local.union(abroad)
print(f"Union set ${friends}")


art = {'Yogeshwar', 'Danush', 'Prathyu'}
engineering = {'Danush', 'Uma', 'Yogeshwar'}

both = art.intersection(engineering)
print(both)