def analyze_image_features(features):
    tips = []

    if "GPSInfo" in features:
        tips.append("GPS data detected — possible exact location available")

    if "DateTime" in features:
        tips.append("Timestamp available — helps estimate time context")

    tips.append("Look for environmental clues: vegetation, architecture, roads")

    return tips
