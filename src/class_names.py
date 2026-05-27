# class_names.py
DISEASE_DETAILS = {
    "Apple___Apple_scab": {
        "vi_name": "🦠 Bệnh Ghẻ Nhám / Đốm Lá Táo",
        "type": "Nấm (Venturia inaequalis)",
        "severity": "Trung bình",
        "symptoms": [
            "Các đốm màu nâu hoặc xanh ô-liu xuất hiện trên bề mặt lá.",
            "Tổn thương làm lá bị xoăn bóp méo, có thể rụng sớm."
        ],
        "causes": [
            "Nấm phát triển mạnh trong điều kiện thời tiết ẩm ướt, mưa nhiều.",
            "Bào tử nấm lây lan qua giọt nước bắn hoặc gió."
        ],
        "treatment": [
            "Thu gom, loại bỏ và tiêu hủy toàn bộ lá bệnh rơi rụng dưới gốc.",
            "Cắt tỉa cành thông thoáng để giảm độ ẩm nội vi của cây.",
            "Sử dụng các loại thuốc diệt nấm gốc đồng (Copper) hoặc hữu cơ khi bệnh nặng."
        ]
    },

    "Apple___Black_rot": {
        "vi_name": "🦠 Bệnh Thối Đen Táo",
        "type": "Nấm (Diplodia seriata / Botryosphaeria obtusa)",
        "severity": "Nặng",
        "symptoms": [
            "Đốm lá hình mắt ếch (frogeye) với tâm nâu và viền tím.",
            "Quả bị thối nâu đen với vòng đồng tâm, thịt quả cứng nhưng thối.",
            "Cành bị loét (canker) đỏ nâu, khô và nứt."
        ],
        "causes": [
            "Nấm tồn tại trong lá rụng, quả khô (mummy) và vết loét trên cành.",
            "Phát triển mạnh trong thời tiết ấm ẩm, cây yếu hoặc bị stress."
        ],
        "treatment": [
            "Thu gom và tiêu hủy lá rụng, quả khô và cành bệnh.",
            "Cắt tỉa cành bệnh, giữ vườn thông thoáng.",
            "Phun thuốc diệt nấm (copper, strobilurin) phòng ngừa từ sau rụng hoa."
        ]
    },

    "Apple___Cedar_apple_rust": {
        "vi_name": "🦠 Bệnh Rỉ Sắt Táo (Cedar Apple Rust)",
        "type": "Nấm (Gymnosporangium juniperi-virginianae)",
        "severity": "Trung bình đến nặng",
        "symptoms": [
            "Đốm vàng cam tròn trên mặt trên lá, sau xuất hiện ống lông nhỏ mặt dưới.",
            "Quả có đốm cam nâu, lá có thể rụng sớm."
        ],
        "causes": [
            "Nấm cần 2 vật chủ: Táo và cây Juniper/Cedar.",
            "Bào tử lan truyền từ cedar sang táo qua gió trong mùa xuân ẩm."
        ],
        "treatment": [
            "Loại bỏ cây cedar/juniper gần vườn táo (trong bán kính 1-2km nếu có thể).",
            "Phun thuốc diệt nấm (myclobutanil, mancozeb) từ giai đoạn nụ hồng.",
            "Chọn giống táo kháng bệnh."
        ]
    },

    "Apple___healthy": {
        "vi_name": "✅ Táo Khỏe mạnh",
        "type": "Bình thường",
        "severity": "Không bệnh",
        "symptoms": [],
        "causes": [],
        "treatment": []
    },

    "Blueberry___healthy": {
        "vi_name": "✅ Việt Quất Khỏe mạnh",
        "type": "Bình thường",
        "severity": "Không bệnh",
        "symptoms": [],
        "causes": [],
        "treatment": []
    },

    "Cherry_(including_sour)___Powdery_mildew": {
        "vi_name": "🦠 Bệnh Phấn Trắng Anh Đào",
        "type": "Nấm (Podosphaera clandestina)",
        "severity": "Trung bình",
        "symptoms": [
            "Lớp bột trắng xám trên lá non, chồi và quả.",
            "Lá bị xoăn, méo mó, quả có vết lõm hoặc bột trắng."
        ],
        "causes": [
            "Thời tiết khô nóng ban ngày, ẩm ban đêm.",
            "Nấm tồn tại trong chồi và lây lan nhanh trên lá non."
        ],
        "treatment": [
            "Cắt tỉa thông thoáng, loại bỏ chồi bệnh.",
            "Phun sulfur hoặc fungicide (SDHI, strobilurin) từ sau rụng hoa.",
            "Tránh tưới lá vào buổi tối."
        ]
    },

    "Cherry_(including_sour)___healthy": {
        "vi_name": "✅ Anh Đào Khỏe mạnh",
        "type": "Bình thường",
        "severity": "Không bệnh",
        "symptoms": [],
        "causes": [],
        "treatment": []
    },

    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "vi_name": "🦠 Bệnh Đốm Lá Xám Ngô (Gray Leaf Spot)",
        "type": "Nấm (Cercospora zeae-maydis)",
        "severity": "Nặng",
        "symptoms": [
            "Vết dài hình chữ nhật, màu xám nâu, giới hạn bởi gân lá.",
            "Lá bị cháy khô nếu nặng."
        ],
        "causes": [
            "Thời tiết ẩm ướt, nhiệt độ ấm.",
            "Nấm tồn tại trên tàn dư cây trồng."
        ],
        "treatment": [
            "Luân canh cây trồng, chôn vùi tàn dư.",
            "Sử dụng giống kháng.",
            "Phun fungicide khi bệnh xuất hiện sớm."
        ]
    },

    "Corn_(maize)___Common_rust_": {
        "vi_name": "🦠 Bệnh Rỉ Sắt Thường Ngô",
        "type": "Nấm (Puccinia sorghi)",
        "severity": "Trung bình",
        "symptoms": [
            "Mụn đỏ nâu (pustules) trên cả hai mặt lá.",
            "Mụn bột khi chạm vào."
        ],
        "causes": [
            "Thời tiết mát ẩm.",
            "Bào tử bay từ miền Nam."
        ],
        "treatment": [
            "Sử dụng giống kháng.",
            "Phun fungicide nếu cần trên giống nhạy cảm."
        ]
    },

    "Corn_(maize)___Northern_Leaf_Blight": {
        "vi_name": "🦠 Bệnh Đốm Lá Phương Bắc Ngô",
        "type": "Nấm (Exserohilum turcicum)",
        "severity": "Nặng",
        "symptoms": [
            "Vết dài hình thuyền hoặc xì gà, màu xám nâu.",
            "Lá bị cháy lớn."
        ],
        "causes": [
            "Thời tiết mát ẩm kéo dài.",
            "Tàn dư cây trồng."
        ],
        "treatment": [
            "Giống kháng, luân canh.",
            "Chôn vùi tàn dư, phun fungicide."
        ]
    },

    "Corn_(maize)___healthy": {
        "vi_name": "✅ Ngô Khỏe mạnh",
        "type": "Bình thường",
        "severity": "Không bệnh",
        "symptoms": [],
        "causes": [],
        "treatment": []
    },

    "Grape___Black_rot": {
        "vi_name": "🦠 Bệnh Thối Đen Nho",
        "type": "Nấm (Guignardia bidwellii)",
        "severity": "Nặng",
        "symptoms": [
            "Đốm nâu tròn trên lá với pycnidia đen.",
            "Quả thối đen, khô cứng như nho khô (mummy)."
        ],
        "causes": [
            "Thời tiết ấm ẩm mùa xuân-hè.",
            "Nấm tồn tại trong quả khô và cành bệnh."
        ],
        "treatment": [
            "Thu gom quả khô và lá bệnh.",
            "Cắt tỉa thông thoáng.",
            "Phun fungicide (captan, myclobutanil) từ trước hoa đến 4 tuần sau."
        ]
    },

    "Grape___Esca_(Black_Measles)": {
        "vi_name": "🦠 Bệnh Esca (Black Measles) Nho",
        "type": "Nấm phức hợp (Phaeomoniella, Phaeoacremonium...)",
        "severity": "Nặng (bệnh thân gỗ)",
        "symptoms": [
            "Lá sọc vàng/đỏ giữa gân (tiger stripe).",
            "Quả có đốm đen nhỏ, cành khô đột ngột (apoplexy)."
        ],
        "causes": [
            "Nấm xâm nhập qua vết cắt tỉa.",
            "Bệnh thân gỗ mãn tính trên cây già."
        ],
        "treatment": [
            "Tránh vết thương lớn khi cắt tỉa.",
            "Phun bảo vệ vết cắt.",
            "Không có cách chữa triệt để, loại bỏ cây nặng."
        ]
    },

    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "vi_name": "🦠 Bệnh Đốm Lá / Cháy Lá Nho (Isariopsis)",
        "type": "Nấm (Pseudocercospora vitis)",
        "severity": "Trung bình",
        "symptoms": [
            "Đốm lớn không đều, đỏ nâu chuyển đen, giòn.",
            "Lá bị cháy nặng cuối mùa."
        ],
        "causes": [
            "Thời tiết ẩm, phổ biến ở vùng nhiệt đới.",
            "Xuất hiện muộn trong mùa."
        ],
        "treatment": [
            "Cắt tỉa thông thoáng.",
            "Phun fungicide theo chương trình phòng ngừa.",
            "Thu gom lá bệnh."
        ]
    },

    "Grape___healthy": {
        "vi_name": "✅ Nho Khỏe mạnh",
        "type": "Bình thường",
        "severity": "Không bệnh",
        "symptoms": [],
        "causes": [],
        "treatment": []
    },

    "Orange___Haunglongbing_(Citrus_greening)": {
        "vi_name": "🦠 Bệnh Greening / Vàng Lá Thối Rễ Cam",
        "type": "Vi khuẩn (Candidatus Liberibacter)",
        "severity": "Rất nặng",
        "symptoms": [
            "Lá loang lổ vàng không đối xứng (blotchy mottle).",
            "Quả nhỏ, méo, đắng, giữ màu xanh một phần."
        ],
        "causes": [
            "Rầy chổng cánh (Asian Citrus Psyllid) truyền bệnh.",
            "Không có cách chữa."
        ],
        "treatment": [
            "Kiểm soát rầy nghiêm ngặt.",
            "Loại bỏ cây bệnh ngay.",
            "Sử dụng cây giống sạch bệnh."
        ]
    },

    "Peach___Bacterial_spot": {
        "vi_name": "🦠 Bệnh Đốm Vi Khuẩn Đào",
        "type": "Vi khuẩn (Xanthomonas arboricola pv. pruni)",
        "severity": "Nặng",
        "symptoms": [
            "Đốm góc cạnh trên lá, tâm rụng tạo lỗ thủng.",
            "Quả có vết lõm đen, nứt, chảy nhựa."
        ],
        "causes": [
            "Thời tiết mưa nhiều, ấm.",
            "Vi khuẩn tồn tại trên chồi và lá."
        ],
        "treatment": [
            "Phun đồng (copper) từ dormant đến sau hoa.",
            "Sử dụng giống kháng.",
            "Cắt tỉa, giữ vườn khô thoáng."
        ]
    },

    "Peach___healthy": {
        "vi_name": "✅ Đào Khỏe mạnh",
        "type": "Bình thường",
        "severity": "Không bệnh",
        "symptoms": [],
        "causes": [],
        "treatment": []
    },

    "Pepper,_bell___Bacterial_spot": {
        "vi_name": "🦠 Bệnh Đốm Vi Khuẩn Ớt Chuông",
        "type": "Vi khuẩn (Xanthomonas spp.)",
        "severity": "Nặng",
        "symptoms": [
            "Đốm nước ngấm trên lá chuyển nâu đen.",
            "Quả có vết sần sùi nâu, nâng cao."
        ],
        "causes": [
            "Hạt giống nhiễm, tưới phun mưa.",
            "Thời tiết ấm ẩm."
        ],
        "treatment": [
            "Dùng hạt giống sạch, giống kháng.",
            "Tránh tưới lá, luân canh.",
            "Phun copper + mancozeb."
        ]
    },

    "Pepper,_bell___healthy": {
        "vi_name": "✅ Ớt Chuông Khỏe mạnh",
        "type": "Bình thường",
        "severity": "Không bệnh",
        "symptoms": [],
        "causes": [],
        "treatment": []
    },

    "Potato___Early_blight": {
        "vi_name": "🦠 Bệnh Mốc Sớm Khoai Tây",
        "type": "Nấm (Alternaria solani)",
        "severity": "Trung bình",
        "symptoms": [
            "Đốm đồng tâm hình bia trên lá già.",
            "Lá vàng và rụng từ dưới lên."
        ],
        "causes": [
            "Thời tiết ấm ẩm.",
            "Tàn dư cây trồng."
        ],
        "treatment": [
            "Luân canh, bón phân cân đối.",
            "Phun fungicide (chlorothalonil, mancozeb)."
        ]
    },

    "Potato___Late_blight": {
        "vi_name": "🦠 Bệnh Mốc Muộn Khoai Tây",
        "type": "Nấm (Phytophthora infestans)",
        "severity": "Rất nặng",
        "symptoms": [
            "Vết ướt nước lớn trên lá, viền trắng mốc mặt dưới.",
            "Thân và củ thối nhanh."
        ],
        "causes": [
            "Thời tiết mát ẩm kéo dài.",
            "Lan truyền rất nhanh."
        ],
        "treatment": [
            "Phun phòng ngừa sớm (mancozeb, Ridomil).",
            "Loại bỏ cây bệnh, dùng giống kháng."
        ]
    },

    "Potato___healthy": {
        "vi_name": "✅ Khoai Tây Khỏe mạnh",
        "type": "Bình thường",
        "severity": "Không bệnh",
        "symptoms": [],
        "causes": [],
        "treatment": []
    },

    "Raspberry___healthy": {
        "vi_name": "✅ Mâm Xôi Khỏe mạnh",
        "type": "Bình thường",
        "severity": "Không bệnh",
        "symptoms": [],
        "causes": [],
        "treatment": []
    },

    "Soybean___healthy": {
        "vi_name": "✅ Đậu Nành Khỏe mạnh",
        "type": "Bình thường",
        "severity": "Không bệnh",
        "symptoms": [],
        "causes": [],
        "treatment": []
    },

    "Squash___Powdery_mildew": {
        "vi_name": "🦠 Bệnh Phấn Trắng Bí",
        "type": "Nấm",
        "severity": "Trung bình",
        "symptoms": [
            "Lớp bột trắng trên lá và thân."
        ],
        "causes": [
            "Thời tiết khô nóng xen kẽ ẩm."
        ],
        "treatment": [
            "Phun sulfur hoặc fungicide chuyên dụng.",
            "Giữ thông thoáng."
        ]
    },

    "Strawberry___Leaf_scorch": {
        "vi_name": "🦠 Bệnh Cháy Lá Dâu Tây",
        "type": "Nấm",
        "severity": "Trung bình",
        "symptoms": [
            "Đốm tím đỏ trên lá, cháy mép lá."
        ],
        "causes": [],
        "treatment": [
            "Thu gom lá bệnh.",
            "Phun fungicide."
        ]
    },

    "Strawberry___healthy": {
        "vi_name": "✅ Dâu Tây Khỏe mạnh",
        "type": "Bình thường",
        "severity": "Không bệnh",
        "symptoms": [],
        "causes": [],
        "treatment": []
    },

    "Tomato___Bacterial_spot": {
        "vi_name": "🦠 Bệnh Đốm Vi Khuẩn Cà Chua",
        "type": "Vi khuẩn (Xanthomonas spp.)",
        "severity": "Nặng",
        "symptoms": [
            "Đốm nhỏ đen trên lá, quả có vết sần."
        ],
        "causes": [
            "Hạt giống nhiễm, tưới phun."
        ],
        "treatment": [
            "Hạt sạch, giống kháng.",
            "Tránh tưới lá, phun copper."
        ]
    },

    "Tomato___Early_blight": {
        "vi_name": "🦠 Bệnh Mốc Sớm Cà Chua",
        "type": "Nấm (Alternaria solani)",
        "severity": "Trung bình",
        "symptoms": [
            "Đốm đồng tâm trên lá già."
        ],
        "causes": [],
        "treatment": [
            "Luân canh, phun fungicide."
        ]
    },

    "Tomato___Late_blight": {
        "vi_name": "🦠 Bệnh Mốc Muộn Cà Chua",
        "type": "Nấm (Phytophthora infestans)",
        "severity": "Rất nặng",
        "symptoms": [
            "Vết ướt nước lớn, mốc trắng."
        ],
        "causes": [],
        "treatment": [
            "Phun phòng ngừa, loại bỏ nhanh."
        ]
    },

    "Tomato___Leaf_Mold": {
        "vi_name": "🦠 Bệnh Mốc Lá Cà Chua",
        "type": "Nấm",
        "severity": "Trung bình",
        "symptoms": [
            "Mốc tím mặt dưới lá, lá vàng."
        ],
        "causes": [],
        "treatment": []
    },

    "Tomato___Septoria_leaf_spot": {
        "vi_name": "🦠 Bệnh Đốm Lá Septoria Cà Chua",
        "type": "Nấm",
        "severity": "Trung bình",
        "symptoms": [
            "Đốm nhỏ tròn với tâm đen."
        ],
        "causes": [],
        "treatment": []
    },

    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "vi_name": "🕷️ Nhện Đỏ Hai Điểm Cà Chua",
        "type": "Sâu hại (nhện)",
        "severity": "Trung bình",
        "symptoms": [
            "Lá châm chích vàng, có tơ mịn."
        ],
        "causes": [],
        "treatment": [
            "Phun nước mạnh, dùng thuốc sinh học."
        ]
    },

    "Tomato___Target_Spot": {
        "vi_name": "🦠 Bệnh Đốm Tròn Đồng Tâm Cà Chua",
        "type": "Nấm",
        "severity": "Trung bình",
        "symptoms": [],
        "causes": [],
        "treatment": []
    },

    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "vi_name": "🦠 Bệnh Virus Cuốn Lá Vàng Cà Chua",
        "type": "Virus",
        "severity": "Rất nặng",
        "symptoms": [
            "Lá cuốn vàng, cây lùn, ít quả."
        ],
        "causes": [
            "Rầy trắng truyền virus."
        ],
        "treatment": [
            "Kiểm soát rầy, dùng lưới chắn."
        ]
    },

    "Tomato___Tomato_mosaic_virus": {
        "vi_name": "🦠 Bệnh Virus Mosaik Cà Chua",
        "type": "Virus",
        "severity": "Nặng",
        "symptoms": [
            "Lá loang lổ, méo mó."
        ],
        "causes": [],
        "treatment": [
            "Vệ sinh dụng cụ, giống kháng."
        ]
    },

    "Tomato___healthy": {
        "vi_name": "✅ Cà Chua Khỏe mạnh",
        "type": "Bình thường",
        "severity": "Không bệnh",
        "symptoms": [],
        "causes": [],
        "treatment": []
    }
}