from nutrition.food_data import food_data

def evaluate_menu(detected_items, user):
    if user.daily_calories == 0:
        return "⚠️ Ingresa tu perfil para recibir recomendaciones."

    response = []
    total_cal = 0

    for food, qty in detected_items.items():
        if food not in food_data:
            continue

        data = food_data[food]
        food_cal = data["cal"] * qty
        total_cal += food_cal

        # Evaluación según objetivo
        good = user.goal in data["best_for"]

        response.append(f"🍽️ Alimento detectado: {food}")
        response.append(f"🔥 Calorías estimadas: {int(food_cal)} kcal")

        if good:
            response.append("✅ Este alimento es ADECUADO para tu objetivo.")
        else:
            response.append("⚠️ Este alimento NO es ideal para tu objetivo.")

        response.append("👍 Ventajas:")
        for p in data["pros"]:
            response.append(f"  • {p}")

        response.append("⚠️ Desventajas:")
        for c in data["cons"]:
            response.append(f"  • {c}")

        response.append(f"🥗 Beneficio principal: Alto aporte de "
                        f"{'proteína' if data['protein'] > 20 else 'energía'}")

        response.append(f"🍴 Menú recomendado: {data['menu']}")
        response.append("")

    # Evaluación global
    response.append("📊 Evaluación total")
    response.append(f"Calorías totales estimadas: {int(total_cal)} kcal")
    response.append(f"Objetivo diario: {user.daily_calories} kcal")

    if total_cal > user.daily_calories * 0.6:
        response.append("🔴 Esta comida es alta para una sola ingesta.")
    else:
        response.append("🟢 Esta comida está dentro de un rango adecuado.")

    return "\n".join(response)
