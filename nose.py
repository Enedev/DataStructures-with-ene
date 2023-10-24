def organizar_solicitudes(cola_solicitudes):
    cola_lotes = {}
    
    while cola_solicitudes:
        solicitud, prioridad = cola_solicitudes.pop()
        
        if prioridad in cola_lotes:
            cola_lotes[prioridad].append(solicitud)
        else:
            cola_lotes[prioridad] = [solicitud]
    
    return cola_lotes

# Ejemplo de cola_solicitudes
cola_solicitudes = [["Solicitud1", 1], ["Solicitud2", 1], ["Solicitud3", 1], ["Solicitud4", 2], ["Solicitud5", 3], ["Solicitud6", 1], ["Solicitud7", 3]]

cola_lotes = organizar_solicitudes(cola_solicitudes)

for prioridad, solicitudes in cola_lotes.items():
    print(f'Lote {prioridad}: {solicitudes}')

print(cola_solicitudes)