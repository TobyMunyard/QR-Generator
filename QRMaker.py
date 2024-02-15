import segno

def generate_qr(content):
    qr = segno.make_qr(content)
    qr.save(content + ".png",scale = 5)

def generate_qr(content, QR_Scale):
    qr = segno.make_qr(content)
    qr.save(
        content + ".png",
        scale = QR_Scale
    )

def generate_qr(content, QR_Scale, color):
    qr = segno.make_qr(content)
    qr.save(
        content + ".png",
        scale = QR_Scale,
        dark = color
    )

def generate_qr(content, QR_Scale, backColor):
    qr = segno.make_qr(content)
    qr.save(
        content + ".png",
        scale = QR_Scale,
        light = backColor
    )

def generate_qr(content, QR_Scale, color, backColor):
    qr = segno.make_qr(content)
    qr.save(
        content + ".png",
        scale = QR_Scale,
        light = backColor,
        dark = color
    )

def generate_qr(content, QR_Scale, color, backColor, darkData):
    qr = segno.make_qr(content)
    qr.save(
        content + ".png",
        scale = QR_Scale,
        light = backColor,
        dark = color,
        data_dark = darkData
    )

def generate_qr(content, QR_Scale, color, backColor, darkData, lightData):
    qr = segno.make_qr(content)
    qr.save(
        content + ".png",
        scale = QR_Scale,
        light = backColor,
        dark = color,
        data_dark = darkData,
        data_light = lightData
    )

def generate_rotated_qr(content, rotation):
    qr = segno.make_qr(content)
    qr_rotated = qr.to_pil(
        ).rotate(rotation)
    qr_rotated.save(content + ".png")

def generate_rotated_qr(content, QR_Scale, rotation):
    qr = segno.make_qr(content)
    qr_rotated = qr.to_pil(
        scale = QR_Scale,
        ).rotate(rotation)
    qr_rotated.save(content + ".png")

def generate_rotated_qr(content, QR_Scale, color, rotation):
    qr = segno.make_qr(content)
    qr_rotated = qr.to_pil(
        scale = QR_Scale,
        dark = color,
        ).rotate(rotation)
    qr_rotated.save(content + ".png")

def generate_rotated_qr(content, QR_Scale, backColor, rotation):
    qr = segno.make_qr(content)
    qr_rotated = qr.to_pil(
        scale = QR_Scale,
        light = backColor,
        ).rotate(rotation)
    qr_rotated.save(content + ".png")

def generate_rotated_qr(content, QR_Scale, color, backColor, rotation):
    qr = segno.make_qr(content)
    qr_rotated = qr.to_pil(
        scale = QR_Scale,
        light = backColor,
        dark = color,
        ).rotate(rotation)
    qr_rotated.save(content + ".png")

def generate_rotated_qr(content, QR_Scale, color, backColor, darkData, rotation):
    qr = segno.make_qr(content)
    qr_rotated = qr.to_pil(
        scale = QR_Scale,
        light = backColor,
        dark = color,
        data_dark = darkData,
        ).rotate(rotation)
    qr_rotated.save(content + ".png")

def generate_rotated_qr(content, QR_Scale, color, backColor, lightData, rotation):
    qr = segno.make_qr(content)
    qr_rotated = qr.to_pil(
        scale = QR_Scale,
        light = backColor,
        dark = color,
        data_light = lightData
        ).rotate(rotation)
    qr_rotated.save(content + ".png")

def generate_rotated_qr(content, QR_Scale, color, backColor, darkData, lightData, rotation):
    qr = segno.make_qr(content)
    qr_rotated = qr.to_pil(
        scale = QR_Scale,
        light = backColor,
        dark = color,
        data_dark = darkData,
        data_light = lightData
        ).rotate(rotation)
    qr_rotated.save(content + ".png")