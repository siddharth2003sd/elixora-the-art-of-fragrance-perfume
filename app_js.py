APP_JS = """  <!-- Application Logic -->
  <script>
    /* ==========================================================
       ÉLIXORA — HAUTE PARFUMERIE SCRIPT ENGINE
       ========================================================== */

    // 1. Master Product Dataset (12+ Luxury Fragrances)
    const PRODUCTS = [
      {
        id: "p1",
        brand: "ÉLIXORA",
        name: "Golden Elixir",
        category: "ORIENTAL",
        gender: "UNISEX",
        concentration: "Extrait de Parfum",
        price: 14999,
        rating: 5,
        sizes: ["50ml", "100ml", "150ml"],
        image: "/golden_elixir.jpg",
        description: "An opulent stream of golden amber, warm cashmeran woods, and honeyed saffron threads, radiating an irresistible, seductive warmth.",
        topNotes: "Saffron · Amberwood · Bergamot",
        heartNotes: "Molten Honey · Moroccan Rose · Incense",
        baseNotes: "Aged Oud · Cashmeran Woods · Vanilla Resins",
        season: "winter",
        occasion: "Evening Gala",
        isBestseller: true
      },
      {
        id: "p2",
        brand: "ÉLIXORA",
        name: "Azure Mist",
        category: "FRESH",
        gender: "UNISEX",
        concentration: "Eau de Parfum",
        price: 9999,
        rating: 4.9,
        sizes: ["50ml", "100ml", "150ml"],
        image: "/azure_mist.jpg",
        description: "A refreshing splash of ocean mist, sea salt, and sun-lit Calabrian bergamot, grounded in clean coastal driftwood.",
        topNotes: "Calabrian Bergamot · Frosted Mint · Sea Salt",
        heartNotes: "White Jasmine · Marine Accord · Lime Blossom",
        baseNotes: "Driftwood · Clean Musk · Ambroxan",
        season: "summer",
        occasion: "Everyday",
        isBestseller: false
      },
      {
        id: "p3",
        brand: "ÉLIXORA",
        name: "Rose Éclat",
        category: "FLORAL",
        gender: "WOMEN",
        concentration: "Eau de Parfum",
        price: 11499,
        rating: 5,
        sizes: ["30ml", "50ml", "100ml"],
        image: "/rose_eclat.jpg",
        description: "Grasse May roses plucked at first light, wrapped in juicy raspberry nectar and warm white musk.",
        topNotes: "Pink Pepper · Mandarin · Bulgarian Rose",
        heartNotes: "Centifolia Rose · Peony · Raspberry Nectar",
        baseNotes: "Bourbon Vanilla · White Amber · Soft Cedar",
        season: "spring",
        occasion: "Date Night",
        isBestseller: true
      },
      {
        id: "p4",
        brand: "ÉLIXORA",
        name: "Noir Intense",
        category: "WOODY",
        gender: "MEN",
        concentration: "Extrait de Parfum",
        price: 15499,
        rating: 4.9,
        sizes: ["50ml", "100ml"],
        image: "/noir_intense.jpg",
        description: "Sultry black leather, smoky oud, and dark violet leaves, crafting an unforgettable trail of mystery.",
        topNotes: "Black Pepper · Violet Leaves · Thyme",
        heartNotes: "Smoked Agarwood · Cistus Labdanum · Tobacco Leaf",
        baseNotes: "Leather Accord · Patchouli · Amber Resins",
        season: "autumn",
        occasion: "Special Occasion",
        isBestseller: true
      },
      {
        id: "p5",
        brand: "ÉLIXORA",
        name: "Emerald Woods",
        category: "WOODY",
        gender: "UNISEX",
        concentration: "Eau de Parfum",
        price: 12499,
        rating: 4.8,
        sizes: ["50ml", "100ml"],
        image: "/emerald_woods.jpg",
        description: "A crisp morning stroll through towering pine and cedar forests, accented by wild mint leaves and green moss.",
        topNotes: "Wild Mint · Juniper Berries · Pine Needle",
        heartNotes: "Atlas Cedar · Florentine Iris · Cypress",
        baseNotes: "Sandalwood · Oakmoss · Vetiver",
        season: "autumn",
        occasion: "Office",
        isBestseller: false
      },
      {
        id: "p6",
        brand: "ÉLIXORA",
        name: "Royal Amethyst",
        category: "ORIENTAL",
        gender: "WOMEN",
        concentration: "Parfum",
        price: 13800,
        rating: 4.9,
        sizes: ["50ml", "100ml"],
        image: "/royal_amethyst.jpg",
        description: "Imperial purple iris butter combined with rich warm patchouli and golden vanilla beans for high-class elegance.",
        topNotes: "Aldehydes · Bergamot · Neroli",
        heartNotes: "Iris Pallida · Grasse Jasmine · Lavender Absolute",
        baseNotes: "Patchouli · Bourbon Vanilla · Golden Amber",
        season: "spring",
        occasion: "Wedding",
        isBestseller: false
      },
      {
        id: "p7",
        brand: "ÉLIXORA",
        name: "Pure Crystal",
        category: "FRESH",
        gender: "UNISEX",
        concentration: "Eau de Parfum",
        price: 10500,
        rating: 4.8,
        sizes: ["50ml", "100ml"],
        image: "/pure_crystal.jpg",
        description: "Pristine clear aldehydic notes, clean linen, and soft white wood, capturing the essence of ultimate purity.",
        topNotes: "Sicilian Petitgrain · Mandora · Aldehydic Accord",
        heartNotes: "Orange Blossom Absolute · Clean Linen Accord",
        baseNotes: "Musk Velvet · Blond Woods · White Cedar",
        season: "spring",
        occasion: "Everyday",
        isBestseller: false
      },
      {
        id: "p8",
        brand: "ÉLIXORA",
        name: "Rouge Passion",
        category: "ORIENTAL",
        gender: "UNISEX",
        concentration: "Extrait de Parfum",
        price: 15800,
        rating: 5,
        sizes: ["70ml", "100ml"],
        image: "/rouge_passion.jpg",
        description: "Vibrant wild cherry, spicy cinnamon bark, and rich smoked tonka bean, igniting an energetic crimson passion.",
        topNotes: "Wild Cherry · Almond · Saffron",
        heartNotes: "Cinnamon Bark · Rose Grandiflorum · Plum",
        baseNotes: "Smoked Tonka · Cedarwood · Sandalwood",
        season: "winter",
        occasion: "Evening Gala",
        isBestseller: true
      },
      {
        id: "p9",
        brand: "ÉLIXORA",
        name: "Aqua Lumière",
        category: "CITRUS",
        gender: "UNISEX",
        concentration: "Eau de Parfum",
        price: 10800,
        rating: 4.9,
        sizes: ["50ml", "100ml"],
        image: "/aqua_lumiere.jpg",
        description: "Sparkling Sicilian mandarin and zesty key lime resting on a bed of fresh ocean water and marine minerals.",
        topNotes: "Sicilian Mandarin · Key Lime · Basil Leaves",
        heartNotes: "Orange Blossom · Peony · Marine Notes",
        baseNotes: "Ozone Accord · Sandalwood · Soft Honey",
        season: "summer",
        occasion: "Daytime",
        isBestseller: true
      },
      {
        id: "p10",
        brand: "ÉLIXORA",
        name: "Peach Blossom",
        category: "FLORAL",
        gender: "WOMEN",
        concentration: "Parfum",
        price: 12800,
        rating: 4.7,
        sizes: ["100ml"],
        image: "/peach_blossom.jpg",
        description: "Soft peach-nude velvet apricot skins, delicate cherry blossoms, and a creamy comforting cocoon of vanilla milk.",
        topNotes: "Velvet Apricot · Soft Peach · Freesia",
        heartNotes: "Cherry Blossom · Jasmine Petals · Cacao Pod",
        baseNotes: "Vanilla Milk · Smoked Tonka · Cashmere Musk",
        season: "winter",
        occasion: "Evening",
        isBestseller: false
      },
      {
        id: "p11",
        brand: "ÉLIXORA",
        name: "Green Oud",
        category: "WOODY",
        gender: "MEN",
        concentration: "Extrait de Parfum",
        price: 17500,
        rating: 4.9,
        sizes: ["50ml", "100ml"],
        image: "/green_oud.jpg",
        description: "Deep Indonesian patchouli, dark oakmoss, and precious green agarwood, creating a profoundly earthy forest trail.",
        topNotes: "Bergamot · Blackcurrant · Pine Balsam",
        heartNotes: "Green Tea · Oakmoss · Marine Accord",
        baseNotes: "Green Agarwood · Sandalwood · Patchouli",
        season: "autumn",
        occasion: "Active Luxury",
        isBestseller: false
      },
      {
        id: "p12",
        brand: "ÉLIXORA",
        name: "Lavender Dream",
        category: "FRESH",
        gender: "UNISEX",
        concentration: "Cologne Intense",
        price: 11900,
        rating: 4.8,
        sizes: ["50ml", "100ml"],
        image: "/lavender_dream.jpg",
        description: "A soothing twilight breeze of French lavender buds, fresh garden sage, and soft comforting white musk.",
        topNotes: "Sea Salt · Ambrette Seeds · Lavender",
        heartNotes: "Sage Herb · Lily of the Valley · Freesia",
        baseNotes: "Driftwood · White Musk · Clean Cedar",
        season: "spring",
        occasion: "Everyday",
        isBestseller: true
      },
      {
        id: "p13",
        brand: "ÉLIXORA",
        name: "Desert Gold",
        category: "ORIENTAL",
        gender: "UNISEX",
        concentration: "Parfum",
        price: 16800,
        rating: 4.9,
        sizes: ["50ml", "100ml"],
        image: "/desert_gold.jpg",
        description: "Warm desert sands, exotic myrrh, toasted cardamoms, and molten amber, capturing the allure of the East.",
        topNotes: "Cardamom · Saffron · Bergamot",
        heartNotes: "Myrrh Resin · Warm Amber · Frankincense",
        baseNotes: "Sandalwood · Cedarwood · Ambergris",
        season: "autumn",
        occasion: "Evening",
        isBestseller: true
      },
      {
        id: "p14",
        brand: "ÉLIXORA",
        name: "Sapphire Noir",
        category: "WOODY",
        gender: "MEN",
        concentration: "Eau de Parfum",
        price: 13500,
        rating: 4.8,
        sizes: ["50ml", "100ml"],
        image: "/sapphire_noir.jpg",
        description: "Noble blue cedarwood, deep vetiver, and crisp mineral ambergris, projecting absolute confidence and modern class.",
        topNotes: "Pink Pepper · Bergamot · Juniper",
        heartNotes: "Blue Cedarwood · Jasmine · Vetiver",
        baseNotes: "Ambergris · Mineral Musk · Patchouli",
        season: "winter",
        occasion: "Office",
        isBestseller: false
      },
      {
        id: "p15",
        brand: "ÉLIXORA",
        name: "Ivory Musk",
        category: "FLORAL",
        gender: "WOMEN",
        concentration: "Eau de Parfum",
        price: 12500,
        rating: 4.9,
        sizes: ["50ml", "100ml"],
        image: "/ivory_musk.jpg",
        description: "An angelic bouquet of white lilies, soft jasmine petals, and warm ivory cashmere musk, timeless and pure.",
        topNotes: "White Lilies · Pear · Aldehydes",
        heartNotes: "Jasmine Petals · Gardenia · Cashmere",
        baseNotes: "Ivory Musk · Sandalwood · Cedar",
        season: "spring",
        occasion: "Everyday",
        isBestseller: false
      },
      {
        id: "p16",
        brand: "ÉLIXORA",
        name: "Silver Mist",
        category: "FRESH",
        gender: "UNISEX",
        concentration: "Eau de Parfum",
        price: 11500,
        rating: 4.7,
        sizes: ["50ml", "100ml"],
        image: "/silver_mist.jpg",
        description: "Sleek metallic aldehydes, cold mineral water, and frosted white tea leaves, designing a chic, futuristic chill.",
        topNotes: "Frosted Aldehydes · Cold Mineral Accord",
        heartNotes: "White Tea Leaves · Freesia · Mint",
        baseNotes: "Silver Musk · Vetiver · Cedar",
        season: "summer",
        occasion: "Everyday",
        isBestseller: false
      },
      {
        id: "p17",
        brand: "ÉLIXORA",
        name: "Coral Bliss",
        category: "CITRUS",
        gender: "UNISEX",
        concentration: "Eau de Toilette",
        price: 9800,
        rating: 4.8,
        sizes: ["50ml", "100ml"],
        image: "/coral_bliss.jpg",
        description: "Vibrant pink grapefruit, energetic blood orange, and sweet passion fruit nectar, bursting with sunshine.",
        topNotes: "Pink Grapefruit · Blood Orange · Lime",
        heartNotes: "Passion Fruit · Peony · Mint Leaves",
        baseNotes: "Soft Musk · Coconut Nectar · Sandalwood",
        season: "summer",
        occasion: "Daytime",
        isBestseller: false
      },
      {
        id: "p18",
        brand: "ÉLIXORA",
        name: "Amethyst Rose",
        category: "FLORAL",
        gender: "WOMEN",
        concentration: "Parfum",
        price: 14500,
        rating: 4.9,
        sizes: ["50ml", "100ml"],
        image: "/amethyst_rose.jpg",
        description: "A royal blend of dark damask rose petals, velvet purple berries, and warm vanilla agarwood.",
        topNotes: "Purple Berries · Plum · Red Currant",
        heartNotes: "Damask Rose · Violet Flowers · Orris",
        baseNotes: "Vanilla Agarwood · Amber · Cashmeran",
        season: "winter",
        occasion: "Evening Gala",
        isBestseller: true
      },
      {
        id: "p19",
        brand: "ÉLIXORA",
        name: "Ocean Veil",
        category: "FRESH",
        gender: "UNISEX",
        concentration: "Cologne",
        price: 8900,
        rating: 4.8,
        sizes: ["50ml", "100ml"],
        image: "/ocean_veil.jpg",
        description: "A weightless mist of sea foam, dewy green leaves, and soft mineral ozone, light and airy as a morning breeze.",
        topNotes: "Sea Foam · Ozone Accord · Dewy Green Leaves",
        heartNotes: "White Freesia · Lily · Cyclamen",
        baseNotes: "Mineral Musk · Driftwood · Ambergris",
        season: "summer",
        occasion: "Everyday",
        isBestseller: false
      },
      {
        id: "p20",
        brand: "ÉLIXORA",
        name: "Café Noir",
        category: "GOURMAND",
        gender: "UNISEX",
        concentration: "Extrait de Parfum",
        price: 15900,
        rating: 5,
        sizes: ["50ml", "100ml"],
        image: "/cafe_noir.jpg",
        description: "Roasted espresso beans, dark cacao pods, caramelized maple wood, and warm aged rum, creating a deep gourmand addiction.",
        topNotes: "Roasted Espresso · Dark Rum · Hazelnut",
        heartNotes: "Cacao Pod · Caramelized Maple · Nutmeg",
        baseNotes: "Smoked Tonka · Guaiac Wood · Cedar",
        season: "autumn",
        occasion: "Evening",
        isBestseller: true
      }
    ];

    // 2. Persistent State
    let cart = JSON.parse(localStorage.getItem("elixora_cart") || "[]");
    let wishlist = JSON.parse(localStorage.getItem("elixora_wishlist") || "[]");
    let compareList = JSON.parse(localStorage.getItem("elixora_compare") || "[]");
    // Filter to ensure only valid product IDs are stored
    compareList = compareList.filter(id => PRODUCTS.some(p => p.id === id));
    let currentFilter = "ALL";
    let currentSort = "featured";
    let activeModalProduct = null;
    let activeConcentrationMultiplier = 1.0;
    let activeSizeMultiplier = 1.0;
    let activeConcentrationName = "EDP";
    let activeSizeName = "100ml";

    // 3. Atmosphere & Ambient Engine (Music option removed as requested)

    // 4. Custom Luxury Cursor
    const cursor = document.getElementById("custom-cursor");
    const cursorFollower = document.getElementById("custom-cursor-follower");
    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let followerX = mouseX;
    let followerY = mouseY;

    window.addEventListener("mousemove", (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      if (cursor) {
        cursor.style.left = `${mouseX}px`;
        cursor.style.top = `${mouseY}px`;
      }
    });

    function animateCursorFollower() {
      followerX += (mouseX - followerX) * 0.15;
      followerY += (mouseY - followerY) * 0.15;
      if (cursorFollower) {
        cursorFollower.style.left = `${followerX}px`;
        cursorFollower.style.top = `${followerY}px`;
      }
      requestAnimationFrame(animateCursorFollower);
    }
    animateCursorFollower();

    function setupCursorInteractions() {
      if (!cursorFollower || !cursorFollower.classList) return;
      const interactives = document.querySelectorAll("button, a, .collection-card, .mood-card, .ingredient-card, .brand-item, select, .compare-action-btn");
      interactives.forEach(el => {
        el.addEventListener("mouseenter", () => {
          if (cursorFollower && cursorFollower.classList) cursorFollower.classList.add("hovering");
        });
        el.addEventListener("mouseleave", () => {
          if (cursorFollower && cursorFollower.classList) cursorFollower.classList.remove("hovering");
        });
      });

      const productCards = document.querySelectorAll(".product-card, .featured-glass-card");
      productCards.forEach(el => {
        el.addEventListener("mouseenter", () => {
          if (cursorFollower && cursorFollower.classList) {
            cursorFollower.classList.add("view-mode");
            cursorFollower.textContent = "VIEW";
          }
        });
        el.addEventListener("mouseleave", () => {
          if (cursorFollower && cursorFollower.classList) {
            cursorFollower.classList.remove("view-mode");
            cursorFollower.textContent = "";
          }
        });
      });
    }

    // 5. Atmospheric Canvas Particles with Pointer Force Field
    const canvas = document.getElementById("particles-canvas");
    const ctx = canvas.getContext("2d");
    let canvasW = (canvas.width = window.innerWidth);
    let canvasH = (canvas.height = window.innerHeight);

    window.addEventListener("resize", () => {
      canvasW = canvas.width = window.innerWidth;
      canvasH = canvas.height = window.innerHeight;
    });

    const PARTICLES_COUNT = window.innerWidth < 768 ? 16 : 38;
    const particles = [];

    const PARTICLE_TYPES = ["rosePetal", "goldDust", "amberOrb", "droplet"];

    class FragranceParticle {
      constructor() {
        this.reset(true);
      }
      reset(initial = false) {
        this.x = Math.random() * canvasW;
        this.y = initial ? Math.random() * canvasH : canvasH + 20;
        this.vx = (Math.random() - 0.5) * 0.6;
        this.vy = -(Math.random() * 0.7 + 0.3);
        this.size = Math.random() * 5 + 2.5;
        this.type = PARTICLE_TYPES[Math.floor(Math.random() * PARTICLE_TYPES.length)];
        this.alpha = Math.random() * 0.5 + 0.2;
        this.rotation = Math.random() * Math.PI * 2;
        this.vRot = (Math.random() - 0.5) * 0.02;
      }
      update() {
        this.x += this.vx;
        this.y += this.vy;
        this.rotation += this.vRot;

        // Pointer force field: gentle repulsion
        const dx = this.x - mouseX;
        const dy = this.y - mouseY;
        const dist = Math.sqrt(dx * dx + dy * dy);
        const repelRadius = 140;

        if (dist < repelRadius && dist > 0) {
          const force = (1 - dist / repelRadius) * 2.2;
          this.x += (dx / dist) * force;
          this.y += (dy / dist) * force;
        }

        if (this.y < -30 || this.x < -30 || this.x > canvasW + 30) {
          this.reset();
        }
      }
      draw() {
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(this.rotation);
        ctx.globalAlpha = this.alpha;

        if (this.type === "rosePetal") {
          ctx.fillStyle = "rgba(251, 207, 232, 0.6)";
          ctx.beginPath();
          ctx.ellipse(0, 0, this.size * 1.5, this.size * 0.9, 0, 0, Math.PI * 2);
          ctx.fill();
        } else if (this.type === "goldDust") {
          ctx.fillStyle = "rgba(212, 175, 112, 0.85)";
          ctx.beginPath();
          ctx.arc(0, 0, this.size * 0.6, 0, Math.PI * 2);
          ctx.fill();
        } else if (this.type === "amberOrb") {
          ctx.fillStyle = "rgba(234, 215, 166, 0.5)";
          ctx.beginPath();
          ctx.arc(0, 0, this.size * 0.9, 0, Math.PI * 2);
          ctx.fill();
        } else {
          ctx.fillStyle = "rgba(255, 255, 255, 0.4)";
          ctx.beginPath();
          ctx.arc(0, 0, this.size * 0.5, 0, Math.PI * 2);
          ctx.fill();
        }
        ctx.restore();
      }
    }

    for (let i = 0; i < PARTICLES_COUNT; i++) {
      particles.push(new FragranceParticle());
    }

    function renderParticles() {
      ctx.clearRect(0, 0, canvasW, canvasH);
      particles.forEach(p => {
        p.update();
        p.draw();
      });
      requestAnimationFrame(renderParticles);
    }
    renderParticles();

    // 6. Hero Full-Screen Campaign Photography Subtle Parallax Reaction
    const heroCampaignFullImg = document.getElementById("hero-campaign-full-img");
    const heroCampaignFullImgNext = document.getElementById("hero-campaign-full-img-next");

    if (window.gsap && heroCampaignFullImg) {
      window.addEventListener("mousemove", (e) => {
        const centerX = window.innerWidth / 2;
        const centerY = window.innerHeight / 2;
        const normX = (e.clientX - centerX) / centerX;
        const normY = (e.clientY - centerY) / centerY;

        gsap.to([heroCampaignFullImg, heroCampaignFullImgNext], {
          x: normX * -6,
          y: normY * -4,
          duration: 1.4,
          ease: "power2.out"
        });
      });
    }

    // Press to release note burst
    const releaseScentBtn = document.getElementById("release-scent-btn");
    const heroPerfumeStage = document.getElementById("hero-perfume-carousel-wrap");

    const triggerScentBurst = () => {
      const activeProd = (typeof PRODUCTS !== "undefined" && PRODUCTS[heroCurrentIndex]) ? PRODUCTS[heroCurrentIndex] : null;
      const notesDesc = activeProd ? `${activeProd.topNotes.split(" · ").join(", ")} & ${activeProd.heartNotes.split(" · ").slice(0, 1).join("")}` : "Black Pepper, Blue Iris & Smoked Amber";
      showToast(`Notes of ${notesDesc} unlocked`);
      
      if (window.gsap && heroCampaignFullImg) {
        gsap.fromTo(heroCampaignFullImg, 
          { scale: 1 }, 
          { scale: 1.025, duration: 0.3, yoyo: true, repeat: 1, ease: "power2.out" }
        );
      }
      // Burst particles outward
      particles.forEach(p => {
        p.vx = (Math.random() - 0.5) * 8;
        p.vy = (Math.random() - 0.5) * 8;
      });
    };

    if (releaseScentBtn) {
      releaseScentBtn.addEventListener("click", triggerScentBurst);
    }

    // Make the luxury perfume stage clickable to trigger scent burst (only when not swiping)
    if (heroPerfumeStage) {
      heroPerfumeStage.style.cursor = "pointer";
      heroPerfumeStage.addEventListener("click", (e) => {
        if (window.heroWasSwiped) return;
        triggerScentBurst();
      });
    }

    // 7. Scent Themes & Background Morphing Engine
    const SCENT_THEMES = {
      noir: {
        gradient: "radial-gradient(circle at 50% 45%, #182236 0%, #0d121c 40%, #080a0f 70%, #030305 100%)",
        accent: "#a5b4fc",
        glow: "rgba(165, 180, 252, 0.25)",
        image: "/noir_intense.jpg",
        name: "Noir Intense"
      },
      rose: {
        gradient: "radial-gradient(circle at 50% 45%, #5c1028 0%, #260711 40%, #100307 70%, #050305 100%)",
        accent: "#fbcfe8",
        glow: "rgba(251, 207, 232, 0.3)",
        image: "/rose_eclat.jpg",
        name: "Rose Éclat"
      },
      oud: {
        gradient: "radial-gradient(circle at 50% 45%, #51301b 0%, #211208 40%, #100904 70%, #050302 100%)",
        accent: "#ead7a6",
        glow: "rgba(212, 175, 112, 0.35)",
        image: "/golden_elixir.jpg",
        name: "Golden Elixir"
      },
      aqua: {
        gradient: "radial-gradient(circle at 50% 45%, #0b4f63 0%, #062b37 40%, #03151c 70%, #020708 100%)",
        accent: "#67e8f9",
        glow: "rgba(103, 232, 249, 0.3)",
        image: "/azure_mist.jpg",
        name: "Azure Mist"
      }
    };

    // Hero Signature Perfume Carousel State Engine with 20-Perfume Map
    const THEME_DATA = {
      p1: { // Amber Gold
        bg: "radial-gradient(circle at 50% 50%, #D4AF37 0%, #5C4017 60%, #150E04 100%)",
        accent: "#D4AF37",
        mood: "warm, luxurious, sensual"
      },
      p2: { // Ocean Blue
        bg: "radial-gradient(circle at 50% 50%, #0077BE 0%, #003366 60%, #001122 100%)",
        accent: "#0077BE",
        mood: "fresh, aquatic, elegant"
      },
      p3: { // Rose Pink
        bg: "radial-gradient(circle at 50% 50%, #FF66CC 0%, #881144 60%, #220311 100%)",
        accent: "#FF66CC",
        mood: "romantic, floral, feminine"
      },
      p4: { // Midnight Black
        bg: "radial-gradient(circle at 50% 50%, #333333 0%, #111111 60%, #000000 100%)",
        accent: "#888888",
        mood: "bold, mysterious, premium"
      },
      p5: { // Emerald Green
        bg: "radial-gradient(circle at 50% 50%, #50C878 0%, #0B5324 60%, #031409 100%)",
        accent: "#50C878",
        mood: "earthy, pine, refreshing"
      },
      p6: { // Royal Purple
        bg: "radial-gradient(circle at 50% 50%, #7851A9 0%, #301934 60%, #0D0410 100%)",
        accent: "#7851A9",
        mood: "royal, powder, elegant"
      },
      p7: { // Crystal Clear
        bg: "radial-gradient(circle at 50% 50%, #E0F2FE 0%, #475569 60%, #0F172A 100%)",
        accent: "#BAE6FD",
        mood: "pure, laundry, clean"
      },
      p8: { // Ruby Red
        bg: "radial-gradient(circle at 50% 50%, #E0115F 0%, #700224 60%, #200007 100%)",
        accent: "#E0115F",
        mood: "passionate, warm, spicy"
      },
      p9: { // Turquoise
        bg: "radial-gradient(circle at 50% 50%, #30D5C8 0%, #006064 60%, #002528 100%)",
        accent: "#30D5C8",
        mood: "zesty, summer, radiant"
      },
      p10: { // Peach Nude
        bg: "radial-gradient(circle at 50% 50%, #FFDAB9 0%, #855030 60%, #28140B 100%)",
        accent: "#FFDAB9",
        mood: "velvety, soft, comforting"
      },
      p11: { // Forest Green
        bg: "radial-gradient(circle at 50% 50%, #228B22 0%, #0B330B 60%, #020F02 100%)",
        accent: "#228B22",
        mood: "earthy, resinous, dark"
      },
      p12: { // Lavender
        bg: "radial-gradient(circle at 50% 50%, #B57EDC 0%, #481E60 60%, #14041C 100%)",
        accent: "#B57EDC",
        mood: "calm, twilight, soothing"
      },
      p13: { // Golden Sand
        bg: "radial-gradient(circle at 50% 50%, #E3A857 0%, #6E4717 60%, #1F1103 100%)",
        accent: "#E3A857",
        mood: "sandy, smoky, exotic"
      },
      p14: { // Sapphire Blue
        bg: "radial-gradient(circle at 50% 50%, #0F52BA 0%, #07255E 60%, #01061C 100%)",
        accent: "#0F52BA",
        mood: "confident, crisp, classic"
      },
      p15: { // Ivory White
        bg: "radial-gradient(circle at 50% 50%, #FDFBF7 0%, #8C8275 60%, #1A1815 100%)",
        accent: "#FDFBF7",
        mood: "angelic, powdery, luxurious"
      },
      p16: { // Silver
        bg: "radial-gradient(circle at 50% 50%, #C0C0C0 0%, #53565A 60%, #111417 100%)",
        accent: "#C0C0C0",
        mood: "frosty, metallic, modern"
      },
      p17: { // Coral
        bg: "radial-gradient(circle at 50% 50%, #FF7F50 0%, #902E0E 60%, #250A02 100%)",
        accent: "#FF7F50",
        mood: "bursting, tropical, sunny"
      },
      p18: { // Amethyst Pink
        bg: "radial-gradient(circle at 50% 50%, #E68FAC 0%, #6D2A43 60%, #230913 100%)",
        accent: "#E68FAC",
        mood: "royal, damask, dark"
      },
      p19: { // Sea Foam
        bg: "radial-gradient(circle at 50% 50%, #9FE2BF 0%, #2A684C 60%, #061B11 100%)",
        accent: "#9FE2BF",
        mood: "weightless, dewy, light"
      },
      p20: { // Espresso Brown
        bg: "radial-gradient(circle at 50% 50%, #4B3621 0%, #26140A 60%, #0D0502 100%)",
        accent: "#4B3621",
        mood: "roasted, boozy, addictive"
      }
    };

    let heroCarouselTimer = null;
    let heroCurrentIndex = 0;
    let isHeroTransitioning = false;
    let isHeroHovered = false;
    let activeBgLayer = 1;
    let activeAuraLayer = 1;

    function initHeroPerfumeCarousel() {
      const wrapper = document.getElementById("hero-perfume-carousel-wrap");
      const prevBtn = document.getElementById("hero-carousel-prev-btn");
      const nextBtn = document.getElementById("hero-carousel-next-btn");
      const dotsContainer = document.getElementById("hero-carousel-dots");

      if (dotsContainer) {
        dotsContainer.innerHTML = "";
        PRODUCTS.forEach((p, idx) => {
          const dot = document.createElement("button");
          dot.className = "hero-dot" + (idx === 0 ? " active" : "");
          dot.setAttribute("data-idx", idx);
          dot.title = p.name;
          dot.onclick = (e) => {
            e.stopPropagation();
            goToHeroSlide(idx);
            resetHeroAutoAdvance();
          };
          dotsContainer.appendChild(dot);
        });
      }

      function goToHeroSlide(index) {
        if (isHeroTransitioning) return;
        heroCurrentIndex = (index + PRODUCTS.length) % PRODUCTS.length;
        
        // Update dots state
        const dots = dotsContainer ? dotsContainer.querySelectorAll(".hero-dot") : [];
        dots.forEach((dot, idx) => {
          dot.classList.toggle("active", idx === heroCurrentIndex);
        });

        applyTheme(PRODUCTS[heroCurrentIndex].id, false);
      }

      function nextHeroSlide() {
        goToHeroSlide(heroCurrentIndex + 1);
      }

      function prevHeroSlide() {
        goToHeroSlide(heroCurrentIndex - 1);
      }

      if (nextBtn) {
        nextBtn.onclick = (e) => {
          e.stopPropagation();
          nextHeroSlide();
          resetHeroAutoAdvance();
        };
      }
      if (prevBtn) {
        prevBtn.onclick = (e) => {
          e.stopPropagation();
          prevHeroSlide();
          resetHeroAutoAdvance();
        };
      }

      function startHeroAutoAdvance() {
        if (heroCarouselTimer) clearInterval(heroCarouselTimer);
        heroCarouselTimer = setInterval(() => {
          // Only auto-advance if the user is currently viewing the hero section
          const isHeroInView = window.scrollY < (window.innerHeight * 0.7);
          if (!isHeroHovered && isHeroInView) {
            nextHeroSlide();
          }
        }, 5500); // Luxury 5.5-second pace
      }

      function resetHeroAutoAdvance() {
        startHeroAutoAdvance();
      }

      window.stopHeroAutoAdvance = function() {
        if (heroCarouselTimer) {
          clearInterval(heroCarouselTimer);
          heroCarouselTimer = null;
        }
      };

      startHeroAutoAdvance();

      // Pause/resume auto-advance on mouse hover for user-guided exploration
      if (wrapper) {
        wrapper.onmouseenter = () => { isHeroHovered = true; };
        wrapper.onmouseleave = () => { isHeroHovered = false; };
      }

      // Touch & Swipe gestures for Hero Fragrances (swiping changes slides, preventing browser back navigation)
      let heroTouchStartX = 0;
      let heroTouchStartY = 0;
      let heroTouchEndX = 0;
      let heroTouchEndY = 0;
      let isHeroTouchActive = false;
      window.heroWasSwiped = false;

      const heroStageEl = document.getElementById("hero") || wrapper;
      if (heroStageEl) {
        heroStageEl.addEventListener("touchstart", (e) => {
          if (e.touches.length > 1) return;
          heroTouchStartX = e.touches[0].clientX;
          heroTouchStartY = e.touches[0].clientY;
          heroTouchEndX = heroTouchStartX;
          heroTouchEndY = heroTouchStartY;
          isHeroTouchActive = true;
        }, { passive: true });

        heroStageEl.addEventListener("touchmove", (e) => {
          if (!isHeroTouchActive || e.touches.length > 1) return;
          heroTouchEndX = e.touches[0].clientX;
          heroTouchEndY = e.touches[0].clientY;
          const diffX = heroTouchEndX - heroTouchStartX;
          const diffY = heroTouchEndY - heroTouchStartY;
          if (Math.abs(diffX) > 12 && Math.abs(diffX) > Math.abs(diffY)) {
            window.heroWasSwiped = true;
          }
        }, { passive: true });

        heroStageEl.addEventListener("touchend", () => {
          if (!isHeroTouchActive) return;
          isHeroTouchActive = false;
          const diffX = heroTouchEndX - heroTouchStartX;
          const diffY = heroTouchEndY - heroTouchStartY;
          if (Math.abs(diffX) > 38 && Math.abs(diffX) > Math.abs(diffY)) {
            window.heroWasSwiped = true;
            if (diffX < 0) {
              nextHeroSlide();
            } else {
              prevHeroSlide();
            }
            resetHeroAutoAdvance();
          }
          setTimeout(() => { window.heroWasSwiped = false; }, 250);
        }, { passive: true });
      }

      // Sync first product on load
      setTimeout(() => {
        applyTheme(PRODUCTS[0].id, false);
      }, 100);

      // Expose function to slide hero carousel when a theme pill is clicked
      window.syncHeroCarouselToTheme = function(themeKey) {
        let resolvedKey = themeKey;
        if (themeKey === "noir") resolvedKey = "p4";
        else if (themeKey === "rose") resolvedKey = "p3";
        else if (themeKey === "oud") resolvedKey = "p1";
        else if (themeKey === "aqua") resolvedKey = "p2";

        const idx = PRODUCTS.findIndex(p => p.id === resolvedKey);
        if (idx !== -1) {
          goToHeroSlide(idx);
          resetHeroAutoAdvance();
        }
      };
    }

    function applyTheme(themeKey, syncHero = true, isManual = false) {
      let resolvedKey = themeKey;
      if (themeKey === "noir") resolvedKey = "p4";
      else if (themeKey === "rose") resolvedKey = "p3";
      else if (themeKey === "oud") resolvedKey = "p1";
      else if (themeKey === "aqua") resolvedKey = "p2";

      const product = PRODUCTS.find(p => p.id === resolvedKey) || PRODUCTS[0];
      const theme = THEME_DATA[product.id] || THEME_DATA.p1;

      // Prevent simultaneous conflicting transitions
      isHeroTransitioning = true;
      setTimeout(() => { isHeroTransitioning = false; }, 450);

      // 1. Dual-Layer Smooth Backdrop Morph
      const layer1 = document.getElementById("bg-layer-1");
      const layer2 = document.getElementById("bg-layer-2");
      if (layer1 && layer2) {
        if (activeBgLayer === 1) {
          layer2.style.background = theme.bg;
          if (window.gsap) {
            gsap.to(layer2, { opacity: 1, duration: 0.45, ease: "power2.out" });
            gsap.to(layer1, { opacity: 0, duration: 0.45, ease: "power2.out" });
          } else {
            layer2.style.opacity = "1";
            layer1.style.opacity = "0";
          }
          activeBgLayer = 2;
        } else {
          layer1.style.background = theme.bg;
          if (window.gsap) {
            gsap.to(layer1, { opacity: 1, duration: 0.45, ease: "power2.out" });
            gsap.to(layer2, { opacity: 0, duration: 0.45, ease: "power2.out" });
          } else {
            layer1.style.opacity = "1";
            layer2.style.opacity = "0";
          }
          activeBgLayer = 1;
        }
      }

      // 3. Luxurious Editorial Typography Cross-fade
      const txtBrand = document.getElementById("hero-dynamic-brand");
      const txtName = document.getElementById("hero-dynamic-name");
      const badgeCategory = document.getElementById("hero-dynamic-category");
      const badgeMood = document.getElementById("hero-dynamic-mood");
      const txtDesc = document.getElementById("hero-dynamic-desc");
      const discoverBtn = document.getElementById("hero-discover-btn");

      const textGroup = [txtBrand, txtName, badgeCategory, badgeMood, txtDesc];
      
      if (window.gsap && txtName) {
        gsap.to(textGroup, {
          opacity: 0,
          y: -10,
          duration: 0.15,
          stagger: 0.015,
          ease: "power2.in",
          onComplete: () => {
            if (txtBrand) txtBrand.textContent = `ÉLIXORA · ${product.brand === "ÉLIXORA" ? "LUXURY" : product.brand.toUpperCase()}`;
            if (txtName) txtName.textContent = product.name.toUpperCase();
            if (badgeCategory) badgeCategory.textContent = product.category.toUpperCase();
            if (badgeMood) badgeMood.textContent = theme.mood;
            if (txtDesc) txtDesc.textContent = product.description;
            if (discoverBtn) {
              discoverBtn.onclick = (e) => {
                e.stopPropagation();
                openProductModal(product.id);
              };
            }

            gsap.to(textGroup, {
              opacity: 1,
              y: 0,
              duration: 0.3,
              stagger: 0.02,
              ease: "power2.out"
            });
          }
        });
      } else {
        if (txtBrand) txtBrand.textContent = `ÉLIXORA · LUXURY`;
        if (txtName) txtName.textContent = product.name.toUpperCase();
        if (badgeCategory) badgeCategory.textContent = product.category.toUpperCase();
        if (badgeMood) badgeMood.textContent = theme.mood;
        if (txtDesc) txtDesc.textContent = product.description;
        if (discoverBtn) {
          discoverBtn.onclick = () => openProductModal(product.id);
        }
      }

      // 4. Hero Full-Screen Campaign Image Cross-fade (Full Viewport Cover, No Circles, Perfectly Fitted)
      const currentFullImg = document.getElementById("hero-campaign-full-img");
      const nextFullImg = document.getElementById("hero-campaign-full-img-next");
      // All 20 fragrance aura themes (p1 through p20) have dedicated seamless widescreen compositions
      const heroSrc = `/hero_wide_${product.id}.jpg`;
      
      if (currentFullImg) {
        if (nextFullImg && window.gsap) {
          nextFullImg.src = heroSrc;
          nextFullImg.alt = `ÉLIXORA ${product.name} Eau de Parfum`;
          gsap.to(nextFullImg, {
            opacity: 1,
            duration: 0.45,
            ease: "power2.out",
            onComplete: () => {
              currentFullImg.src = heroSrc;
              currentFullImg.alt = `ÉLIXORA ${product.name} Eau de Parfum`;
              gsap.set(nextFullImg, { opacity: 0 });
            }
          });
        } else {
          currentFullImg.src = heroSrc;
          currentFullImg.alt = `ÉLIXORA ${product.name} Eau de Parfum`;
        }
      }

      // Backwards sync compatible mode
      if (syncHero) {
        const dotsContainer = document.getElementById("hero-carousel-dots");
        const idx = PRODUCTS.findIndex(p => p.id === product.id);
        if (idx !== -1) {
          heroCurrentIndex = idx;
          const dots = dotsContainer ? dotsContainer.querySelectorAll(".hero-dot") : [];
          dots.forEach((dot, i) => {
            dot.classList.toggle("active", i === idx);
          });
        }
      }

      // 5. Update active status of the horizontal selector pills without shifting page scroll
      const themePillsWrap = document.querySelector(".theme-pills");
      document.querySelectorAll(".theme-pill-btn").forEach(btn => {
        const btnTheme = btn.getAttribute("data-theme");
        const isActive = (btnTheme === resolvedKey);
        btn.classList.toggle("active", isActive);
        
        if (isActive && isManual && themePillsWrap) {
          const scrollTarget = btn.offsetLeft - (themePillsWrap.clientWidth / 2) + (btn.clientWidth / 2);
          themePillsWrap.scrollTo({ left: scrollTarget, behavior: "smooth" });
        }
      });
    }

    document.querySelectorAll(".theme-pill-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        if (window.stopHeroAutoAdvance) {
          window.stopHeroAutoAdvance();
        }
        applyTheme(btn.getAttribute("data-theme"), true, true);
      });
    });

    function previewIngredientTheme(themeKey) {
      applyTheme(themeKey, true, true);
    }

    // 8. Header Scroll Reduction
    window.addEventListener("scroll", () => {
      const header = document.getElementById("main-header");
      if (header && header.classList) {
        if (window.scrollY > 50) {
          header.classList.add("scrolled");
        } else {
          header.classList.remove("scrolled");
        }
      }
    });

    // 9. Catalog Rendering Engine
    function renderProductCardHTML(p) {
      const isWish = wishlist.some(item => item.id === p.id);
      const isCompared = compareList.includes(p.id);
      return `
        <article class="product-card" onclick="if (!window.carouselWasSwiped) openProductModal('${p.id}')">
          <div class="card-top-actions" onclick="event.stopPropagation()">
            ${p.isBestseller ? '<span class="tag-badge bestseller">Bestseller</span>' : `<span class="tag-badge">${p.category}</span>`}
            <div class="card-action-btns">
              <button class="compare-toggle-btn ${isCompared ? 'active' : ''}" onclick="toggleCompareProduct('${p.id}', event)" title="${isCompared ? 'Remove from Comparison' : 'Compare notes, concentration & price'}" aria-label="Compare ${p.name}">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M16 3h5v5M4 20L21 3M21 16v5h-5M15 15l6 6M4 4l5 5"/>
                </svg>
                <span class="compare-pill-text">${isCompared ? 'Compared' : 'Compare'}</span>
              </button>
              <button class="wishlist-toggle-btn ${isWish ? 'active' : ''}" onclick="toggleWishlist('${p.id}')" aria-label="Save ${p.name}">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="${isWish ? 'currentColor' : 'none'}" stroke="currentColor" stroke-width="2">
                  <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
                </svg>
              </button>
            </div>
          </div>
          <div class="product-img-wrapper">
            <img src="${p.image}" alt="${p.name}" loading="lazy" />
            <button class="quick-view-overlay-btn" onclick="event.stopPropagation(); openProductModal('${p.id}')">QUICK VIEW</button>
          </div>
          <div class="product-info">
            <span class="product-brand">${p.brand}</span>
            <h3 class="product-name">${p.name}</h3>
            <p class="product-family-meta">${p.category} &middot; ${p.concentration}</p>
            <div class="product-rating-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
            <div class="product-bottom-row" onclick="event.stopPropagation()">
              <span class="product-price-val">₹${p.price.toLocaleString("en-IN")}</span>
              <button class="add-to-bag-btn" onclick="addToCart('${p.id}', '${p.concentration}', '100ml', ${p.price})">ADD TO BAG</button>
            </div>
          </div>
        </article>
      `;
    }

    // Carousel State Engine (Infinite Loop & Touch/Mouse Swipe & 3s Auto-Advance)
    let catalogCarouselTimer = null;
    let carouselCurrentIndex = 0;
    let carouselCardCount = 0;
    let isCarouselTransitioning = false;
    let carouselDragStartX = 0;
    let carouselCurrentDragX = 0;
    let isCarouselDragging = false;
    let isCarouselHovered = false;

    function getCarouselVisibleCount() {
      const w = window.innerWidth;
      if (w <= 560) return 1;
      if (w <= 860) return 2;
      if (w <= 1200) return 3;
      return 4;
    }

    function initCatalogCarousel(items) {
      const container = document.getElementById("products-grid");
      const wrapper = document.getElementById("products-carousel-wrapper");
      const viewport = document.getElementById("carousel-viewport");
      const dotsWrap = document.getElementById("carousel-dots-wrap");
      const prevBtn = document.getElementById("carousel-prev-btn");
      const nextBtn = document.getElementById("carousel-next-btn");
      const statusText = document.getElementById("carousel-status-text");

      if (!container || !wrapper || items.length === 0) return;

      // Stop previous timer
      if (catalogCarouselTimer) {
        clearInterval(catalogCarouselTimer);
        catalogCarouselTimer = null;
      }

      carouselCardCount = items.length;
      carouselCurrentIndex = 0;

      // Create cloned sets for infinite looping: [Clone Set, Original Set, Clone Set]
      // This guarantees seamless wrap-around at both boundaries
      const originalHTML = items.map(p => renderProductCardHTML(p)).join("");
      container.innerHTML = originalHTML + originalHTML + originalHTML;

      // Start at first item of middle (original) set
      carouselCurrentIndex = carouselCardCount;

      setupCursorInteractions();

      // Setup dots
      if (dotsWrap) {
        dotsWrap.innerHTML = items.map((_, i) => `
          <button class="carousel-dot ${i === 0 ? 'active' : ''}" data-idx="${i}" aria-label="Go to fragrance ${i + 1}"></button>
        `).join("");

        dotsWrap.querySelectorAll(".carousel-dot").forEach(dot => {
          dot.addEventListener("click", () => {
            const targetIdx = parseInt(dot.getAttribute("data-idx"), 10);
            goToCarouselIndex(carouselCardCount + targetIdx, true);
          });
        });
      }

      function updateCarouselPosition(animate = true) {
        const firstCard = container.querySelector(".product-card");
        if (!firstCard) return;
        const cardWidth = firstCard.offsetWidth;
        const gap = 32; // 2rem = 32px
        const step = cardWidth + gap;
        const offset = -(carouselCurrentIndex * step);

        if (animate) {
          container.style.transition = "transform 0.65s cubic-bezier(0.16, 1, 0.3, 1)";
        } else {
          container.style.transition = "none";
        }
        container.style.transform = `translateX(${offset}px)`;

        // Update dots
        if (dotsWrap) {
          const activeDotIdx = ((carouselCurrentIndex % carouselCardCount) + carouselCardCount) % carouselCardCount;
          dotsWrap.querySelectorAll(".carousel-dot").forEach((d, i) => {
            d.classList.toggle("active", i === activeDotIdx);
          });
        }
      }

      function handleBoundaryLoop() {
        // If moved past the middle set to the right clone set
        if (carouselCurrentIndex >= carouselCardCount * 2) {
          carouselCurrentIndex = carouselCardCount;
          updateCarouselPosition(false);
        }
        // If moved past the middle set to the left clone set
        else if (carouselCurrentIndex < carouselCardCount) {
          carouselCurrentIndex = carouselCardCount * 2 - 1;
          updateCarouselPosition(false);
        }
        isCarouselTransitioning = false;
      }

      container.removeEventListener("transitionend", container._boundTransitionEnd);
      container._boundTransitionEnd = () => handleBoundaryLoop();
      container.addEventListener("transitionend", container._boundTransitionEnd);

      function goToCarouselIndex(index, animate = true) {
        if (isCarouselTransitioning && animate) return;
        if (animate) isCarouselTransitioning = true;
        carouselCurrentIndex = index;
        updateCarouselPosition(animate);
      }

      function nextSlide() {
        goToCarouselIndex(carouselCurrentIndex + 1, true);
      }

      function prevSlide() {
        goToCarouselIndex(carouselCurrentIndex - 1, true);
      }

      // Button controls
      if (nextBtn) {
        nextBtn.onclick = () => {
          nextSlide();
          resetAutoAdvance();
        };
      }
      if (prevBtn) {
        prevBtn.onclick = () => {
          prevSlide();
          resetAutoAdvance();
        };
      }

      // Initial alignment
      setTimeout(() => {
        updateCarouselPosition(false);
      }, 50);

      // Auto-advance every 3.5 seconds only when catalog is visible
      function startAutoAdvance() {
        if (catalogCarouselTimer) clearInterval(catalogCarouselTimer);
        catalogCarouselTimer = setInterval(() => {
          const catalogEl = document.getElementById("catalog");
          const isCatalogInView = catalogEl ? (
            catalogEl.getBoundingClientRect().top < window.innerHeight &&
            catalogEl.getBoundingClientRect().bottom > 0
          ) : false;
          if (!isCarouselHovered && !isCarouselDragging && isCatalogInView) {
            nextSlide();
          }
        }, 3500);
        if (statusText) statusText.textContent = "Auto-Advancing every 3.5s";
      }

      function resetAutoAdvance() {
        startAutoAdvance();
      }

      startAutoAdvance();

      // Pause on hover
      wrapper.onmouseenter = () => {
        isCarouselHovered = true;
        if (statusText) statusText.textContent = "Paused on Hover";
      };
      wrapper.onmouseleave = () => {
        isCarouselHovered = false;
        if (statusText) statusText.textContent = "Auto-Advancing every 3s";
      };

      // Touch & Mouse Drag / Swipe Handlers
      let carouselDragStartY = 0;
      let carouselCurrentDragY = 0;
      let isHorizontalTouch = null;
      window.carouselWasSwiped = false;

      viewport.onmousedown = (e) => {
        if (e.target.closest("button") || e.target.closest(".quick-view-overlay-btn")) return;
        isCarouselDragging = true;
        carouselDragStartX = e.clientX;
        carouselCurrentDragX = e.clientX;
        carouselDragStartY = e.clientY;
        carouselCurrentDragY = e.clientY;
        container.style.transition = "none";
      };

      window.addEventListener("mousemove", (e) => {
        if (!isCarouselDragging) return;
        carouselCurrentDragX = e.clientX;
        carouselCurrentDragY = e.clientY;
        const diffX = carouselCurrentDragX - carouselDragStartX;
        if (Math.abs(diffX) > 8) {
          window.carouselWasSwiped = true;
        }
        const firstCard = container.querySelector(".product-card");
        if (!firstCard) return;
        const step = firstCard.offsetWidth + 32;
        const baseOffset = -(carouselCurrentIndex * step);
        container.style.transform = `translateX(${baseOffset + diffX}px)`;
      });

      window.addEventListener("mouseup", (e) => {
        if (!isCarouselDragging) return;
        isCarouselDragging = false;
        const diffX = carouselCurrentDragX - carouselDragStartX;
        if (Math.abs(diffX) > 10) {
          window.carouselWasSwiped = true;
          setTimeout(() => { window.carouselWasSwiped = false; }, 250);
        }
        if (diffX < -50) {
          nextSlide();
        } else if (diffX > 50) {
          prevSlide();
        } else {
          updateCarouselPosition(true);
        }
        resetAutoAdvance();
      });

      // Mobile Touch Events with vertical scroll protection
      viewport.addEventListener("touchstart", (e) => {
        if (e.touches.length > 1) return;
        isCarouselDragging = true;
        isHorizontalTouch = null;
        carouselDragStartX = e.touches[0].clientX;
        carouselCurrentDragX = e.touches[0].clientX;
        carouselDragStartY = e.touches[0].clientY;
        carouselCurrentDragY = e.touches[0].clientY;
        container.style.transition = "none";
      }, { passive: true });

      viewport.addEventListener("touchmove", (e) => {
        if (!isCarouselDragging || e.touches.length > 1) return;
        carouselCurrentDragX = e.touches[0].clientX;
        carouselCurrentDragY = e.touches[0].clientY;
        const diffX = carouselCurrentDragX - carouselDragStartX;
        const diffY = carouselCurrentDragY - carouselDragStartY;

        if (isHorizontalTouch === null && (Math.abs(diffX) > 6 || Math.abs(diffY) > 6)) {
          isHorizontalTouch = Math.abs(diffX) > Math.abs(diffY);
        }

        // If vertical scrolling, let the page scroll naturally
        if (isHorizontalTouch === false) {
          return;
        }

        if (Math.abs(diffX) > 8) {
          window.carouselWasSwiped = true;
        }

        const firstCard = container.querySelector(".product-card");
        if (!firstCard) return;
        const step = firstCard.offsetWidth + 32;
        const baseOffset = -(carouselCurrentIndex * step);
        container.style.transform = `translateX(${baseOffset + diffX}px)`;
      }, { passive: true });

      viewport.addEventListener("touchend", () => {
        if (!isCarouselDragging) return;
        isCarouselDragging = false;
        const diffX = carouselCurrentDragX - carouselDragStartX;
        if (Math.abs(diffX) > 10) {
          window.carouselWasSwiped = true;
          setTimeout(() => { window.carouselWasSwiped = false; }, 250);
        }
        if (isHorizontalTouch !== false) {
          if (diffX < -45) {
            nextSlide();
          } else if (diffX > 45) {
            prevSlide();
          } else {
            updateCarouselPosition(true);
          }
        }
        isHorizontalTouch = null;
        resetAutoAdvance();
      }, { passive: true });

      // Responsive resize repositioning
      window.addEventListener("resize", () => {
        updateCarouselPosition(false);
      });
    }

    function renderCatalog() {
      let filtered = [...PRODUCTS];

      if (currentFilter !== "ALL") {
        if (["MEN", "WOMEN", "UNISEX"].includes(currentFilter)) {
          filtered = filtered.filter(p => p.gender === currentFilter);
        } else if (currentFilter === "bestseller") {
          filtered = filtered.filter(p => p.isBestseller);
        } else {
          filtered = filtered.filter(p => p.category.toUpperCase() === currentFilter.toUpperCase());
        }
      }

      // Sort
      if (currentSort === "price-asc") {
        filtered.sort((a, b) => a.price - b.price);
      } else if (currentSort === "price-desc") {
        filtered.sort((a, b) => b.price - a.price);
      } else if (currentSort === "rating") {
        filtered.sort((a, b) => b.rating - a.rating);
      }

      // Initialize the auto-advancing infinite looping carousel
      initCatalogCarousel(filtered);
    }

    // Filter by button
    document.querySelectorAll("#catalog-filter-pills .filter-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        document.querySelectorAll("#catalog-filter-pills .filter-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        currentFilter = btn.getAttribute("data-filter");
        renderCatalog();
      });
    });

    // Sort select
    const catalogSortSelect = document.getElementById("catalog-sort-select");
    if (catalogSortSelect) {
      catalogSortSelect.addEventListener("change", (e) => {
        currentSort = e.target.value;
        renderCatalog();
      });
    }

    function filterCatalogBy(family) {
      currentFilter = family.toUpperCase();
      document.querySelectorAll("#catalog-filter-pills .filter-btn").forEach(b => {
        b.classList.toggle("active", b.getAttribute("data-filter") === currentFilter);
      });
      renderCatalog();
    }

    function filterCatalogByBrand(brand) {
      const filtered = PRODUCTS.filter(p => p.brand.toUpperCase() === brand.toUpperCase());
      initCatalogCarousel(filtered);
      showToast(`Showing creations by ${brand}`);
    }

    // 10. Seasonal Section Logic (Strict Season-Wise Unique Fragrances, No Repetition)
    const SEASON_PROFILES = {
      autumn: {
        title: "Autumn Harmonies · 5 Exclusive Fragrances",
        tagline: "Warm Woods, Smoky Agarwood, Saffron Sands & Roasted Espresso",
        desc: "Curated for crisp breezes and twilight contemplation. Rich resinous bases, warm spices, and amber textures that project gracefully in cool air."
      },
      winter: {
        title: "Winter Splendour · 5 Exclusive Fragrances",
        tagline: "Golden Amber, Candied Rose, Royal Incense & Cashmere Nectar",
        desc: "Decadent, enveloping extraits designed for celebratory evenings and cold nights. Intensely concentrated sillage with royal warmth."
      },
      spring: {
        title: "Spring Awakening · 5 Exclusive Fragrances",
        tagline: "Grasse May Rose, Florentine Iris, Orange Blossom & Provence Lavender",
        desc: "Bright, dewy botanicals and powdery floral silks echoing newborn blossoms, Mediterranean groves, and sunlit mornings."
      },
      summer: {
        title: "Summer Solar & Marine · 5 Exclusive Fragrances",
        tagline: "Mediterranean Sea Salt, Mandarin Waves, Frosted Tea & Coral Fruits",
        desc: "Weightless crystalline aquatics, frosted minerals, and vibrant citrus accords engineered for refreshing endurance in tropical heat."
      }
    };

    function renderSeasonalSection(season = "autumn") {
      const container = document.getElementById("seasonal-products-grid");
      const descEl = document.getElementById("seasonal-desc-content");
      if (!container) return;

      const normalizedSeason = (season || "autumn").toLowerCase();
      // Strictly unique fragrances for each season: NO overlap or repetition with other seasons
      const filtered = PRODUCTS.filter(p => p.season.toLowerCase() === normalizedSeason);
      container.innerHTML = filtered.map(p => renderProductCardHTML(p)).join("");

      if (descEl && SEASON_PROFILES[normalizedSeason]) {
        const prof = SEASON_PROFILES[normalizedSeason];
        descEl.innerHTML = `
          <div class="seasonal-banner-badge">
            <span class="seasonal-badge-title">${prof.title}</span>
            <span class="seasonal-badge-tagline">${prof.tagline}</span>
            <p class="seasonal-badge-desc">${prof.desc}</p>
          </div>
        `;
      }
      setupCursorInteractions();
    }

    document.querySelectorAll(".seasonal-tab-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        document.querySelectorAll(".seasonal-tab-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        const season = btn.getAttribute("data-season");
        renderSeasonalSection(season);
      });
    });

    // 11. Fullscreen Product Detail Modal & Variants
    function openProductModal(productId) {
      const product = PRODUCTS.find(p => p.id === productId);
      if (!product) return;

      activeModalProduct = product;
      activeConcentrationMultiplier = 1.0;
      activeSizeMultiplier = 1.0;
      activeConcentrationName = "EDP";
      activeSizeName = "100ml";

      document.getElementById("modal-product-img").src = product.image;
      document.getElementById("modal-brand-label").textContent = product.brand;
      document.getElementById("modal-title-label").textContent = product.name;
      document.getElementById("modal-desc-label").textContent = product.description;
      document.getElementById("modal-top-notes").textContent = product.topNotes;
      document.getElementById("modal-heart-notes").textContent = product.heartNotes;
      document.getElementById("modal-base-notes").textContent = product.baseNotes;

      updateModalPricing();

      // Reset variant pill states
      document.querySelectorAll("#modal-concentration-pills .variant-pill").forEach(p => {
        p.classList.toggle("active", p.textContent.includes("EDP"));
      });
      document.querySelectorAll("#modal-size-pills .variant-pill").forEach(p => {
        p.classList.toggle("active", p.textContent.includes("100ml"));
      });

      const modal = document.getElementById("product-detail-modal");
      modal.classList.add("active");
      document.body.style.overflow = "hidden";

      // Animate Fragrance Pyramid with GSAP
      if (window.gsap) {
        gsap.from(".pyramid-tier", {
          opacity: 0,
          x: -20,
          stagger: 0.15,
          duration: 0.5,
          delay: 0.2,
          ease: "power2.out"
        });
      }
    }

    function closeProductModal() {
      const modal = document.getElementById("product-detail-modal");
      modal.classList.remove("active");
      document.body.style.overflow = "";
    }

    function closeProductModalOnBackdrop(e) {
      if (e.target.id === "product-detail-modal") {
        closeProductModal();
      }
    }

    function selectConcentration(name, multiplier) {
      activeConcentrationName = name;
      activeConcentrationMultiplier = multiplier;
      document.querySelectorAll("#modal-concentration-pills .variant-pill").forEach(p => {
        p.classList.toggle("active", p.textContent.trim().startsWith(name));
      });
      updateModalPricing();
    }

    function selectSize(size, multiplier) {
      activeSizeName = size;
      activeSizeMultiplier = multiplier;
      document.querySelectorAll("#modal-size-pills .variant-pill").forEach(p => {
        p.classList.toggle("active", p.textContent.includes(size));
      });
      updateModalPricing();
    }

    function updateModalPricing() {
      if (!activeModalProduct) return;
      const calculatedPrice = Math.round(activeModalProduct.price * activeConcentrationMultiplier * activeSizeMultiplier);
      const formatted = `₹${calculatedPrice.toLocaleString("en-IN")}`;
      document.getElementById("modal-price-label").textContent = formatted;
      document.getElementById("modal-btn-price").textContent = formatted;
    }

    function toggleModalEngraveInput(checked) {
      const container = document.getElementById("modal-engrave-input-container");
      if (container) container.style.display = checked ? "block" : "none";
    }

    function addActiveModalToBag() {
      if (!activeModalProduct) return;
      const calculatedPrice = Math.round(activeModalProduct.price * activeConcentrationMultiplier * activeSizeMultiplier);
      const engraveCheckbox = document.getElementById("modal-engrave-checkbox");
      const engraveInput = document.getElementById("modal-engrave-input-text");
      const engraving = (engraveCheckbox && engraveCheckbox.checked && engraveInput && engraveInput.value.trim()) 
        ? engraveInput.value.trim().toUpperCase() 
        : null;

      addToCart(activeModalProduct.id, activeConcentrationName, activeSizeName, calculatedPrice, engraving);
      if (engraveInput) engraveInput.value = "";
      if (engraveCheckbox) engraveCheckbox.checked = false;
      toggleModalEngraveInput(false);
      closeProductModal();
      openCartDrawer();
    }

    function toggleActiveModalWishlist() {
      if (!activeModalProduct) return;
      toggleWishlist(activeModalProduct.id);
    }

    // 13. Shopping Cart Mechanics (localStorage persistent)
    let cartDiscountPercent = 0;
    let appliedCouponCode = "";

    function applyCartCoupon() {
      const input = document.getElementById("cart-coupon-input");
      const resultBadge = document.getElementById("cart-coupon-result");
      if (!input || !resultBadge) return;

      const code = input.value.trim().toUpperCase();
      if (!code) {
        resultBadge.style.color = "#ef4444";
        resultBadge.textContent = "Please enter a valid coupon code";
        return;
      }

      if (code === "MYOP3FOR2" || code === "BUY2GET1") {
        cartDiscountPercent = 0.33;
        appliedCouponCode = code;
        resultBadge.style.color = "#4ade80";
        resultBadge.textContent = `Coupon ${code} applied: 33% Off (Buy 2 Get 1 Benefit)!`;
        showToast("Offer applied: 33% Savings on Cart!");
      } else if (code === "WELCOME10" || code === "MYOP10") {
        cartDiscountPercent = 0.10;
        appliedCouponCode = code;
        resultBadge.style.color = "#4ade80";
        resultBadge.textContent = `Coupon ${code} applied: 10% Welcome Discount!`;
        showToast("10% Welcome Discount applied!");
      } else if (code === "ELIXORA15") {
        cartDiscountPercent = 0.15;
        appliedCouponCode = code;
        resultBadge.style.color = "#4ade80";
        resultBadge.textContent = `Coupon ${code} applied: 15% VIP Connoisseur Discount!`;
        showToast("15% VIP discount applied!");
      } else {
        resultBadge.style.color = "#ef4444";
        resultBadge.textContent = "Invalid code. Try MYOP3FOR2 or WELCOME10";
        return;
      }
      updateCartUI();
    }

    function checkCartPincode() {
      const input = document.getElementById("cart-pincode-input");
      const result = document.getElementById("cart-pincode-result");
      if (!input || !result) return;
      const pin = input.value.trim();
      if (pin.length !== 6 || isNaN(pin)) {
        result.style.color = "#ef4444";
        result.textContent = "Please enter a valid 6-digit Indian PIN code";
        return;
      }
      result.style.color = "#4ade80";
      result.innerHTML = `&#10003; Express Air Delivery to <strong>${pin}</strong>: Guaranteed by <strong>tomorrow 3:00 PM</strong>.`;
      showToast(`Pincode ${pin} is eligible for Free Express Delivery!`);
    }

    function addToCart(productId, variantConc, variantSize, price, engraving = null) {
      const product = PRODUCTS.find(p => p.id === productId);
      if (!product) return;

      const existingIndex = cart.findIndex(item => 
        item.id === productId && item.concentration === variantConc && item.size === variantSize && item.engraving === engraving
      );

      if (existingIndex > -1) {
        cart[existingIndex].qty += 1;
      } else {
        cart.push({
          id: product.id,
          brand: product.brand,
          name: product.name,
          image: product.image,
          concentration: variantConc,
          size: variantSize,
          price: price,
          engraving: engraving,
          qty: 1
        });
      }

      saveCart();
      showToast(`Added ${product.name} (${variantSize}) to your bag`);
    }

    function updateCartQty(index, delta) {
      if (!cart[index]) return;
      cart[index].qty += delta;
      if (cart[index].qty <= 0) {
        cart.splice(index, 1);
      }
      saveCart();
    }

    function saveCart() {
      localStorage.setItem("elixora_cart", JSON.stringify(cart));
      updateCartUI();
    }

    function updateCartUI() {
      const countBadge = document.getElementById("cart-count-badge");
      const totalCount = cart.reduce((sum, item) => sum + item.qty, 0);
      countBadge.textContent = totalCount;

      const container = document.getElementById("cart-items-container");
      if (cart.length === 0) {
        container.innerHTML = `
          <div style="text-align: center; color: var(--muted-color); padding: 4rem 1rem;">
            <p style="font-size: 1.1rem; margin-bottom: 1.5rem; font-family: var(--heading-font);">Your shopping bag is empty.</p>
            <a href="#catalog" onclick="closeCartDrawer()" class="secondary-btn">Explore Fragrances</a>
          </div>
        `;
        document.getElementById("cart-subtotal-val").textContent = "₹0";
        const discRow = document.getElementById("cart-discount-row");
        if (discRow) discRow.style.display = "none";
        const finalEl = document.getElementById("cart-final-total-val");
        if (finalEl) finalEl.textContent = "₹0";
        return;
      }

      let subtotal = 0;
      container.innerHTML = cart.map((item, idx) => {
        const itemTotal = item.price * item.qty;
        subtotal += itemTotal;
        return `
          <div class="cart-item-row">
            <img class="cart-item-img" src="${item.image}" alt="${item.name}" />
            <div class="cart-item-details">
              <span class="cart-item-brand">${item.brand}</span>
              <h4 class="cart-item-name">${item.name}</h4>
              <p class="cart-item-variant">${item.concentration} &middot; ${item.size}</p>
              ${item.engraving ? `<div style="font-size: 0.72rem; color: var(--gold); margin: 3px 0;">✦ Engraving: "${item.engraving}"</div>` : ""}
              <div class="cart-item-qty-row">
                <div class="qty-controls">
                  <button class="qty-btn" onclick="updateCartQty(${idx}, -1)">&minus;</button>
                  <span class="qty-val">${item.qty}</span>
                  <button class="qty-btn" onclick="updateCartQty(${idx}, 1)">&plus;</button>
                </div>
                <span class="cart-item-price">₹${itemTotal.toLocaleString("en-IN")}</span>
              </div>
            </div>
          </div>
        `;
      }).join("");

      document.getElementById("cart-subtotal-val").textContent = `₹${subtotal.toLocaleString("en-IN")}`;

      const discountAmount = Math.round(subtotal * cartDiscountPercent);
      const finalTotal = Math.max(0, subtotal - discountAmount);

      const discountRow = document.getElementById("cart-discount-row");
      const discountVal = document.getElementById("cart-discount-val");
      if (discountRow && discountVal) {
        if (discountAmount > 0) {
          discountRow.style.display = "flex";
          discountVal.textContent = `-₹${discountAmount.toLocaleString("en-IN")}`;
        } else {
          discountRow.style.display = "none";
        }
      }

      const finalTotalEl = document.getElementById("cart-final-total-val");
      if (finalTotalEl) {
        finalTotalEl.textContent = `₹${finalTotal.toLocaleString("en-IN")}`;
      }
    }

    function openCartDrawer() {
      updateCartUI();
      document.getElementById("cart-drawer-overlay").classList.add("active");
      document.getElementById("cart-drawer-panel").classList.add("active");
    }

    function closeCartDrawer() {
      document.getElementById("cart-drawer-overlay").classList.remove("active");
      document.getElementById("cart-drawer-panel").classList.remove("active");
    }

    document.getElementById("open-cart-btn").addEventListener("click", openCartDrawer);

    function proceedToCheckout() {
      if (cart.length === 0) {
        showToast("Your bag is currently empty");
        return;
      }
      openCheckoutModal();
      closeCartDrawer();
    }

    /* ============================================================
       CHECKOUT MODAL SYSTEM
       ============================================================ */

    function openCheckoutModal() {
      populateCheckoutOrderSummary();
      document.getElementById("checkout-modal").classList.add("active");
      document.body.style.overflow = "hidden";
    }

    function closeCheckoutModal() {
      document.getElementById("checkout-modal").classList.remove("active");
      document.body.style.overflow = "";
    }

    function populateCheckoutOrderSummary() {
      const container = document.getElementById("checkout-order-items");
      let subtotal = 0;

      container.innerHTML = cart.map(item => {
        const itemTotal = item.price * item.qty;
        subtotal += itemTotal;
        return `
          <div class="order-item-row">
            <img class="order-item-thumb" src="${item.image}" alt="${item.name}" />
            <div class="order-item-info">
              <div class="order-item-name">${item.name}</div>
              <div class="order-item-meta">${item.concentration} · ${item.size} × ${item.qty}</div>
            </div>
            <div class="order-item-price">₹${itemTotal.toLocaleString("en-IN")}</div>
          </div>
        `;
      }).join("");

      const discountAmount = Math.round(subtotal * cartDiscountPercent);
      const grandTotal = Math.max(0, subtotal - discountAmount);

      document.getElementById("checkout-subtotal").textContent = `₹${subtotal.toLocaleString("en-IN")}`;
      document.getElementById("checkout-grand-total").textContent = `₹${grandTotal.toLocaleString("en-IN")}`;

      const discRow = document.getElementById("checkout-discount-row");
      const discVal = document.getElementById("checkout-discount-val");
      if (discountAmount > 0) {
        discRow.style.display = "flex";
        discVal.textContent = `-₹${discountAmount.toLocaleString("en-IN")}`;
      } else {
        discRow.style.display = "none";
      }

      // Store grand total for payment modal
      window._checkoutGrandTotal = grandTotal;
    }

    function validateCheckoutForm() {
      const fields = [
        { id: "co-name", errId: "co-name-err", test: v => v.trim().length >= 2 },
        { id: "co-mobile", errId: "co-mobile-err", test: v => /^\d{10}$/.test(v.trim()) },
        { id: "co-email", errId: "co-email-err", test: v => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim()) },
        { id: "co-street", errId: "co-street-err", test: v => v.trim().length >= 5 },
        { id: "co-city", errId: "co-city-err", test: v => v.trim().length >= 2 },
        { id: "co-state", errId: "co-state-err", test: v => v.trim().length >= 2 },
        { id: "co-pincode", errId: "co-pincode-err", test: v => /^\d{6}$/.test(v.trim()) },
      ];

      let valid = true;
      fields.forEach(({ id, errId, test }) => {
        const el = document.getElementById(id);
        const err = document.getElementById(errId);
        if (!el || !err) return;
        const ok = test(el.value);
        if (!ok) {
          el.classList.add("error");
          err.style.display = "block";
          valid = false;
        } else {
          el.classList.remove("error");
          err.style.display = "none";
        }
      });
      return valid;
    }

    function proceedToPayment() {
      if (!validateCheckoutForm()) {
        showToast("Please fill in all required fields correctly");
        return;
      }
      const total = window._checkoutGrandTotal || 0;
      document.getElementById("payment-total-display").textContent = `₹${total.toLocaleString("en-IN")}`;
      document.getElementById("payment-modal").classList.add("active");
    }

    function closePaymentModal() {
      document.getElementById("payment-modal").classList.remove("active");
    }

    /* ============================================================
       PAYMENT METHOD SELECTION
       ============================================================ */
    let _selectedPaymentMethod = "upi";

    function selectPaymentMethod(method) {
      _selectedPaymentMethod = method;

      // Update visual selection
      ["upi", "card", "cod"].forEach(m => {
        const label = document.getElementById(`pm-${m}-label`);
        const radio = document.getElementById(`pm-${m}`);
        if (!label || !radio) return;
        label.classList.toggle("selected", m === method);
        radio.checked = (m === method);
      });

      // Show / hide UPI field
      const upiField = document.getElementById("payment-upi-field");
      const cardFields = document.getElementById("payment-card-fields");

      if (method === "upi") {
        upiField.classList.add("visible");
        cardFields.classList.remove("visible");
      } else if (method === "card") {
        upiField.classList.remove("visible");
        cardFields.classList.add("visible");
      } else {
        upiField.classList.remove("visible");
        cardFields.classList.remove("visible");
      }
    }

    /* Card number formatter */
    const cardNumInput = document.getElementById("payment-card-num");
    if (cardNumInput) {
      cardNumInput.addEventListener("input", function () {
        let val = this.value.replace(/\D/g, "").substring(0, 16);
        this.value = val.replace(/(.{4})/g, "$1 ").trim();
      });
    }

    /* Card expiry formatter */
    const cardExpiryInput = document.getElementById("payment-card-expiry");
    if (cardExpiryInput) {
      cardExpiryInput.addEventListener("input", function () {
        let val = this.value.replace(/\D/g, "").substring(0, 4);
        if (val.length >= 3) val = val.substring(0, 2) + "/" + val.substring(2);
        this.value = val;
      });
    }

    /* ============================================================
       SUBMIT PAYMENT
       ============================================================ */
    function submitPayment() {
      // Basic validation per method
      if (_selectedPaymentMethod === "upi") {
        const upiId = document.getElementById("payment-upi-id").value.trim();
        const upiErr = document.getElementById("payment-upi-err");
        const upiInput = document.getElementById("payment-upi-id");
        if (!upiId || !upiId.includes("@")) {
          upiErr.style.display = "block";
          upiInput.classList.add("error");
          return;
        }
        upiErr.style.display = "none";
        upiInput.classList.remove("error");
      }

      if (_selectedPaymentMethod === "card") {
        const cardNum = document.getElementById("payment-card-num").value.replace(/\s/g, "");
        const cardErr = document.getElementById("payment-card-err");
        const cardInput = document.getElementById("payment-card-num");
        if (cardNum.length < 16) {
          cardErr.style.display = "block";
          cardInput.classList.add("error");
          return;
        }
        cardErr.style.display = "none";
        cardInput.classList.remove("error");
      }

      // Show processing state
      const btn = document.getElementById("pay-now-btn");
      const originalText = btn.innerHTML;
      btn.innerHTML = `<span class="pay-spinner"></span> Processing...`;
      btn.disabled = true;

      // Simulate payment processing
      const processingTime = _selectedPaymentMethod === "cod" ? 800 : 2200;
      setTimeout(() => {
        btn.innerHTML = originalText;
        btn.disabled = false;

        // Generate order ID
        const orderId = "ELX-" + Date.now().toString().slice(-6);
        document.getElementById("success-order-id-display").textContent = orderId;

        // Record into Admin Orders Database
        try {
          const storedOrders = getStoredOrders();
          const newOrderRecord = {
            id: orderId,
            date: new Date().toLocaleString("en-IN", { dateStyle: "medium", timeStyle: "short" }),
            customer: {
              name: _checkoutCustomerDetails?.name || "VIP Collector",
              mobile: _checkoutCustomerDetails?.mobile || "",
              email: _checkoutCustomerDetails?.email || ""
            },
            address: {
              street: _checkoutCustomerDetails?.street || "",
              city: _checkoutCustomerDetails?.city || "",
              state: _checkoutCustomerDetails?.state || "",
              pincode: _checkoutCustomerDetails?.pincode || ""
            },
            items: cart.map(item => ({
              id: item.id,
              name: item.name,
              size: item.size || "100ml",
              qty: item.qty || 1,
              price: item.price
            })),
            paymentMethod: _selectedPaymentMethod.toUpperCase(),
            total: _checkoutGrandTotal || 0,
            status: "Placed",
            awb: `BLUEDART-AIR-${Math.floor(1000000 + Math.random() * 9000000)}`
          };
          storedOrders.unshift(newOrderRecord);
          saveStoredOrders(storedOrders);
        } catch(err) {
          console.error("Order save error:", err);
        }

        // Clear cart
        cart = [];
        saveCart();

        // Close payment modal
        closePaymentModal();
        closeCheckoutModal();

        // Show success
        document.getElementById("order-success-modal").classList.add("active");

      }, processingTime);
    }

    function closeOrderSuccessModal() {
      document.getElementById("order-success-modal").classList.remove("active");
      document.body.style.overflow = "";
    }

    // Close checkout on backdrop click
    document.getElementById("checkout-modal").addEventListener("click", function(e) {
      if (e.target === this) closeCheckoutModal();
    });

    // Close payment on backdrop click
    document.getElementById("payment-modal").addEventListener("click", function(e) {
      if (e.target === this) closePaymentModal();
    });

    // Escape key to close modals
    document.addEventListener("keydown", function(e) {
      if (e.key === "Escape") {
        if (document.getElementById("order-success-modal").classList.contains("active")) {
          closeOrderSuccessModal();
        } else if (document.getElementById("payment-modal").classList.contains("active")) {
          closePaymentModal();
        } else if (document.getElementById("checkout-modal").classList.contains("active")) {
          closeCheckoutModal();
        }
      }
    });

    // 14. Wishlist Mechanics (localStorage persistent)
    function toggleWishlist(productId) {
      const product = PRODUCTS.find(p => p.id === productId);
      if (!product) return;

      const idx = wishlist.findIndex(item => item.id === productId);
      if (idx > -1) {
        wishlist.splice(idx, 1);
        showToast(`Removed ${product.name} from saved items`);
      } else {
        wishlist.push(product);
        showToast(`Saved ${product.name} to your private collection`);
      }

      localStorage.setItem("elixora_wishlist", JSON.stringify(wishlist));
      updateWishlistUI();
      renderCatalog();
    }

    function updateWishlistUI() {
      const countBadge = document.getElementById("wishlist-count-badge");
      countBadge.textContent = wishlist.length;

      const container = document.getElementById("wishlist-items-container");
      if (wishlist.length === 0) {
        container.innerHTML = `
          <div style="text-align: center; color: var(--muted-color); padding: 4rem 1rem;">
            <p style="font-size: 1.1rem; margin-bottom: 1.5rem; font-family: var(--heading-font);">No saved elixirs yet.</p>
            <a href="#catalog" onclick="closeWishlistDrawer()" class="secondary-btn">Browse Collection</a>
          </div>
        `;
        return;
      }

      container.innerHTML = wishlist.map(item => `
        <div class="cart-item-row" style="align-items: center;">
          <img class="cart-item-img" src="${item.image}" alt="${item.name}" />
          <div class="cart-item-details">
            <span class="cart-item-brand">${item.brand}</span>
            <h4 class="cart-item-name">${item.name}</h4>
            <p class="cart-item-variant">${item.category} &middot; ₹${item.price.toLocaleString("en-IN")}</p>
          </div>
          <button class="add-to-bag-btn" onclick="addToCart('${item.id}', '${item.concentration}', '100ml', ${item.price})">Add</button>
        </div>
      `).join("");
    }

    function openWishlistDrawer() {
      updateWishlistUI();
      document.getElementById("wishlist-drawer-overlay").classList.add("active");
      document.getElementById("wishlist-drawer-panel").classList.add("active");
    }

    function closeWishlistDrawer() {
      document.getElementById("wishlist-drawer-overlay").classList.remove("active");
      document.getElementById("wishlist-drawer-panel").classList.remove("active");
    }

    document.getElementById("open-wishlist-btn").addEventListener("click", openWishlistDrawer);

    // 15. Search Overlay Engine
    function openSearchOverlay() {
      document.getElementById("search-overlay").classList.add("active");
      document.getElementById("search-input").focus();
      handleSearchInput({ target: { value: "" } });
    }

    function closeSearchOverlay() {
      document.getElementById("search-overlay").classList.remove("active");
    }

    document.getElementById("open-search-btn").addEventListener("click", openSearchOverlay);

    function handleSearchInput(e) {
      const q = e.target.value.toLowerCase().trim();
      const container = document.getElementById("search-results-grid");

      let filtered = PRODUCTS;
      if (q) {
        filtered = PRODUCTS.filter(p => 
          p.name.toLowerCase().includes(q) ||
          p.brand.toLowerCase().includes(q) ||
          p.category.toLowerCase().includes(q) ||
          p.description.toLowerCase().includes(q) ||
          p.topNotes.toLowerCase().includes(q) ||
          p.heartNotes.toLowerCase().includes(q) ||
          p.baseNotes.toLowerCase().includes(q)
        );
      }

      if (filtered.length === 0) {
        container.innerHTML = `<p style="grid-column: 1/-1; text-align: center; color: var(--muted-color); padding: 2rem;">No elixirs found matching "${q}".</p>`;
      } else {
        container.innerHTML = filtered.slice(0, 6).map(p => `
          <div class="product-card" onclick="closeSearchOverlay(); openProductModal('${p.id}')">
            <div class="product-img-wrapper" style="height: 180px;">
              <img src="${p.image}" alt="${p.name}" />
            </div>
            <div class="product-info">
              <span class="product-brand">${p.brand}</span>
              <h4 class="product-name" style="font-size: 1.1rem;">${p.name}</h4>
              <p class="product-family-meta">${p.category}</p>
              <span class="product-price-val">₹${p.price.toLocaleString("en-IN")}</span>
            </div>
          </div>
        `).join("");
      }
      setupCursorInteractions();
    }

    function quickSearch(term) {
      const input = document.getElementById("search-input");
      input.value = term;
      handleSearchInput({ target: { value: term } });
    }

    // 16. Testimonial Carousel
    let activeSlide = 0;
    const slides = document.querySelectorAll(".testimonial-slide");

    function showSlide(index) {
      slides.forEach((s, idx) => {
        s.classList.toggle("active", idx === index);
      });
    }

    function nextTestimonial() {
      activeSlide = (activeSlide + 1) % slides.length;
      showSlide(activeSlide);
    }

    function prevTestimonial() {
      activeSlide = (activeSlide - 1 + slides.length) % slides.length;
      showSlide(activeSlide);
    }

    // Auto-advance testimonials every 7s
    setInterval(nextTestimonial, 7000);

    // 17. MYOP Bespoke Blending Atelier Engine
    const customStudioState = {
      step: 1,
      flacon: "Noir Facet",
      flaconSize: "100",
      flaconPrice: 3999,
      capFinish: "24k Gold",
      baseOilKey: "oud",
      baseOilName: "Royal Oud Wood",
      heartNotes: ["Damascus Rose"],
      oilConcentration: 50,
      bottleName: "ÉTERNEL ROYAL",
      engravingText: "A & S 2026"
    };

    function switchStudioStep(step) {
      customStudioState.step = step;
      
      // Update Step Panes
      for (let s = 1; s <= 5; s++) {
        const pane = document.getElementById(`studio-step-pane-${s}`);
        if (pane) {
          pane.style.display = (s === step) ? "block" : "none";
        }
      }
      
      // Update Stepper Nav Tabs
      const tabsContainer = document.getElementById("studio-stepper-nav");
      if (tabsContainer) {
        const tabs = tabsContainer.querySelectorAll(".studio-step-tab");
        tabs.forEach((tab, index) => {
          const s = index + 1;
          tab.classList.toggle("active", s === step);
          tab.classList.toggle("completed", s < step);
        });
      }
      
      updateStudioVisualizer();
    }

    function selectStudioFlacon(nameOrSize, sizeOrPrice, maybePriceOrBtn, maybeBtn) {
      let size = "100";
      let price = 2499;
      let btn = null;

      if (typeof nameOrSize === "string") {
        size = nameOrSize.replace(/[^0-9]/g, "") || "100";
      }
      if (typeof sizeOrPrice === "number") {
        price = sizeOrPrice;
      } else if (typeof sizeOrPrice === "string") {
        size = sizeOrPrice.replace(/[^0-9]/g, "") || size;
      }
      if (typeof maybePriceOrBtn === "number") {
        price = maybePriceOrBtn;
      } else if (maybePriceOrBtn && maybePriceOrBtn.classList) {
        btn = maybePriceOrBtn;
      }
      if (maybeBtn && maybeBtn.classList) {
        btn = maybeBtn;
      }

      customStudioState.flacon = `${size}ml Flacon`;
      customStudioState.flaconSize = size;
      customStudioState.flaconPrice = price;

      document.querySelectorAll(".flacon-choice-card, .flacon-option-card").forEach(c => {
        if (c && c.classList) {
          c.classList.remove("active");
          c.classList.remove("selected");
        }
      });
      if (btn && btn.classList) {
        btn.classList.add("active");
        btn.classList.add("selected");
      }
      updateStudioVisualizer();
    }

    function selectStudioFinish(finish, colorOrBtn, maybeBtn) {
      customStudioState.capFinish = finish;
      let btn = null;
      if (maybeBtn && maybeBtn.classList) {
        btn = maybeBtn;
      } else if (colorOrBtn && colorOrBtn.classList) {
        btn = colorOrBtn;
      }

      document.querySelectorAll(".finish-pill-btn, .finish-pill").forEach(p => {
        if (p && p.classList) {
          p.classList.remove("active");
          p.classList.remove("selected");
        }
      });
      if (btn && btn.classList) {
        btn.classList.add("active");
        btn.classList.add("selected");
      }
      updateStudioVisualizer();
    }

    function selectBaseOil(keyOrName, nameOrOrigin, accordOrDesc, colorOrBtn, maybeBtn) {
      const name = (typeof keyOrName === "string" && keyOrName.length > 4) ? keyOrName : (nameOrOrigin || "Sandalwood");
      const lower = name.toLowerCase();
      let key = "sandalwood";
      if (lower.includes("oud")) key = "oud";
      else if (lower.includes("rose")) key = "rose";
      else if (lower.includes("aqua") || lower.includes("salt") || lower.includes("vetiver")) key = "aqua";
      else if (lower.includes("tonka") || lower.includes("amber") || lower.includes("vanilla")) key = "amber";

      customStudioState.baseOilKey = key;
      customStudioState.baseOilName = name;

      let btn = null;
      if (maybeBtn && maybeBtn.classList) {
        btn = maybeBtn;
      } else if (colorOrBtn && colorOrBtn.classList) {
        btn = colorOrBtn;
      }

      document.querySelectorAll(".oil-card, .base-oil-card").forEach(c => {
        if (c && c.classList) {
          c.classList.remove("active");
          c.classList.remove("selected");
        }
      });
      if (btn && btn.classList) {
        btn.classList.add("active");
        btn.classList.add("selected");
      }
      updateStudioVisualizer();
    }

    function toggleHeartNote(note, tagOrBtn, maybeBtn) {
      const btn = (tagOrBtn && tagOrBtn.classList) ? tagOrBtn : ((maybeBtn && maybeBtn.classList) ? maybeBtn : null);
      const idx = customStudioState.heartNotes.indexOf(note);
      if (idx > -1) {
        if (customStudioState.heartNotes.length === 1) {
          showToast("Please keep at least 1 heart note in your formulation");
          return;
        }
        customStudioState.heartNotes.splice(idx, 1);
        if (btn && btn.classList) {
          btn.classList.remove("active");
          btn.classList.remove("selected");
        }
      } else {
        if (customStudioState.heartNotes.length >= 2) {
          showToast("Maximum 2 heart notes allowed for optimum balance");
          return;
        }
        customStudioState.heartNotes.push(note);
        if (btn && btn.classList) {
          btn.classList.add("active");
          btn.classList.add("selected");
        }
      }
      updateStudioVisualizer();
    }

    function selectStudioFont(fontFamily, isItalicOrBtn, maybeBtn) {
      let isItalic = false;
      let btn = null;
      if (typeof isItalicOrBtn === "boolean") {
        isItalic = isItalicOrBtn;
        if (maybeBtn && maybeBtn.classList) btn = maybeBtn;
      } else if (isItalicOrBtn && isItalicOrBtn.classList) {
        btn = isItalicOrBtn;
      }

      const preview = document.getElementById("studio-preview-engraving");
      if (preview) {
        preview.style.fontFamily = fontFamily;
        preview.style.fontStyle = isItalic ? "italic" : "normal";
      }

      document.querySelectorAll(".engrave-font-btn").forEach(b => {
        if (b && b.classList) {
          b.classList.remove("active");
          b.classList.remove("selected");
        }
      });
      if (btn && btn.classList) {
        btn.classList.add("active");
        btn.classList.add("selected");
      }
    }

    function handleStudioRatio(val) {
      customStudioState.oilConcentration = parseInt(val, 10);
      const ratioVal = document.getElementById("ratio-slider-val");
      const oilBar = document.getElementById("studio-oil-fill-bar");
      const alcoholBar = document.getElementById("studio-alcohol-fill-bar");
      if (ratioVal) {
        let tierText = "EDP (20% Oil · 8-10h Sillage)";
        if (customStudioState.oilConcentration >= 45) {
          tierText = "Extrait de Parfum (50% Pure Tropical Oil · 24h+ Long-Lasting)";
        } else if (customStudioState.oilConcentration >= 35) {
          tierText = "Parfum (35% Oil · 14-16h Sillage)";
        }
        ratioVal.textContent = `${customStudioState.oilConcentration}% Oil · ${tierText}`;
      }
      if (oilBar) oilBar.style.width = `${customStudioState.oilConcentration}%`;
      if (alcoholBar) alcoholBar.style.width = `${100 - customStudioState.oilConcentration}%`;
      updateStudioVisualizer();
    }

    function updateCustomBottleName(val) {
      customStudioState.bottleName = val.trim() || "MY BESPOKE BLEND";
      const label = document.getElementById("studio-preview-name");
      if (label) label.textContent = customStudioState.bottleName.toUpperCase();
    }

    function updateCustomEngravingText(val) {
      customStudioState.engravingText = val.trim();
      const label = document.getElementById("studio-preview-engraving");
      if (label) {
        label.textContent = customStudioState.engravingText ? `✦ ${customStudioState.engravingText} ✦` : "✦ LASER ENGRAVING ✦";
      }
    }

    function calculateStudioPrice() {
      const basePrice = customStudioState.flaconPrice || 3999;
      const oilMultiplier = customStudioState.oilConcentration === 50 ? 1.25 : (customStudioState.oilConcentration >= 35 ? 1.15 : 1.0);
      return Math.round(basePrice * oilMultiplier);
    }

    function updateStudioVisualizer() {
      const previewName = document.getElementById("studio-preview-name");
      const previewCap = document.getElementById("studio-preview-cap");
      const previewAccords = document.getElementById("studio-preview-accords");
      const previewPrice = document.getElementById("studio-total-price");
      const bottleImg = document.getElementById("studio-bottle-render-img");

      if (previewName) previewName.textContent = (customStudioState.bottleName || "MY BESPOKE BLEND").toUpperCase();
      if (previewCap) previewCap.textContent = `${customStudioState.capFinish} Collar · ${customStudioState.flaconSize}ml`;

      if (bottleImg) {
        if (customStudioState.flacon.includes("Rose") || customStudioState.baseOilKey === "rose") {
          bottleImg.src = "/elixora_rose_bottle.jpg";
        } else if (customStudioState.flacon.includes("Decanter") || customStudioState.baseOilKey === "aqua") {
          bottleImg.src = "/elixora_aqua_bottle.jpg";
        } else if (customStudioState.baseOilKey === "oud") {
          bottleImg.src = "/elixora_oud_bottle.jpg";
        } else {
          bottleImg.src = "/elixora_hero_bottle.jpg";
        }
      }

      if (previewAccords) {
        const accordsList = [customStudioState.baseOilName, ...customStudioState.heartNotes, `${customStudioState.oilConcentration}% Tropical Oil`];
        previewAccords.innerHTML = accordsList.map(a => `<span class="studio-accord-tag">${a}</span>`).join("");
      }

      const price = calculateStudioPrice();
      if (previewPrice) previewPrice.textContent = `₹${price.toLocaleString("en-IN")}`;
    }

    function addCustomBlendToBag() {
      const price = calculateStudioPrice();
      const bespokeItem = {
        id: `custom_${Date.now()}`,
        brand: "MYOP ATELIER",
        name: customStudioState.bottleName || "Custom Bespoke Blend",
        image: (customStudioState.baseOilKey === "rose") ? "/elixora_rose_bottle.jpg" : ((customStudioState.baseOilKey === "aqua") ? "/elixora_aqua_bottle.jpg" : "/elixora_hero_bottle.jpg"),
        concentration: `50% Tropical Extrait (${customStudioState.baseOilName} + ${customStudioState.heartNotes.join(", ")})`,
        size: `${customStudioState.flaconSize}ml · ${customStudioState.flacon}`,
        price: price,
        engraving: customStudioState.engravingText ? customStudioState.engravingText.toUpperCase() : "Complimentary Laser Engraving",
        qty: 1
      };

      cart.push(bespokeItem);
      saveCart();
      showToast(`Added custom blend "${bespokeItem.name}" to your bag!`);
      openCartDrawer();
    }

    // 18. Bottle Personalisation Studio
    let activePersProduct = PRODUCTS[0];
    let activePersFont = "Playfair Display, serif";
    let activePersFoil = "gold";

    function handlePersonalisePerfumeSelect(productVal) {
      // productVal can be id ("p1") or name ("Éternel Noir")
      let prod = PRODUCTS.find(p => p.id === productVal || p.name.toLowerCase() === productVal.toLowerCase());
      if (!prod && PRODUCTS.length > 0) prod = PRODUCTS[0];
      if (prod) {
        activePersProduct = prod;
        const img1 = document.getElementById("pers-preview-img");
        if (img1) img1.src = prod.image;
        const img2 = document.getElementById("personalise-bottle-preview-img");
        if (img2) img2.src = prod.image;

        const title = document.getElementById("pers-bottle-name");
        if (title) title.textContent = prod.name.toUpperCase();

        const price = document.getElementById("pers-total-price");
        if (price) price.textContent = `₹${prod.price.toLocaleString("en-IN")}`;
        const priceDisp = document.getElementById("personalise-price-display");
        if (priceDisp) priceDisp.textContent = `₹${prod.price.toLocaleString("en-IN")}`;
      }
    }

    function handlePersonaliseTextInput(val) {
      const trimmed = val.trim();
      const textToDisplay = trimmed ? trimmed.toUpperCase() : "YOUR NAME OR INITIALS";
      const label1 = document.getElementById("pers-preview-text");
      if (label1) label1.textContent = textToDisplay;
      const label2 = document.getElementById("personalise-live-text");
      if (label2) {
        label2.textContent = textToDisplay;
        // Dynamically scale font size and letter spacing to fit within bottle boundary
        const len = textToDisplay.length;
        if (len <= 10) {
          label2.style.fontSize = "0.82rem";
          label2.style.letterSpacing = "0.15em";
        } else if (len <= 16) {
          label2.style.fontSize = "0.72rem";
          label2.style.letterSpacing = "0.10em";
        } else {
          label2.style.fontSize = "0.64rem";
          label2.style.letterSpacing = "0.06em";
        }
      }
    }

    function selectPersonaliseFont(font, isItalicOrBtn, maybeBtn) {
      activePersFont = font;
      let isItalic = false;
      let btn = null;

      if (typeof isItalicOrBtn === "boolean") {
        isItalic = isItalicOrBtn;
        if (maybeBtn && maybeBtn.classList) btn = maybeBtn;
      } else if (isItalicOrBtn && isItalicOrBtn.classList) {
        btn = isItalicOrBtn;
      }

      document.querySelectorAll(".font-select-btn, .engrave-font-btn").forEach(b => {
        if (b && b.classList) {
          b.classList.remove("active");
          b.classList.remove("selected");
        }
      });
      if (btn && btn.classList) {
        btn.classList.add("active");
        btn.classList.add("selected");
      }
      const labels = [document.getElementById("pers-preview-text"), document.getElementById("personalise-live-text")];
      labels.forEach(label => {
        if (label) {
          label.style.fontFamily = font;
          label.style.fontStyle = isItalic ? "italic" : "normal";
        }
      });
    }

    function selectFoilFinish(foil, btn) {
      activePersFoil = foil;
      document.querySelectorAll(".foil-option-pill, .foil-btn").forEach(p => {
        if (p && p.classList) {
          p.classList.remove("active");
          p.classList.remove("selected");
        }
      });
      if (btn && btn.classList) {
        btn.classList.add("active");
        btn.classList.add("selected");
      }
      const labels = [document.getElementById("pers-preview-text"), document.getElementById("personalise-live-text")];
      labels.forEach(label => {
        if (label) {
          if (foil === "silver" || foil === "#e2e8f0") {
            label.style.color = "#f1f5f9";
            label.style.textShadow = "0 1px 2px rgba(0,0,0,0.9), 0 0 10px rgba(241, 245, 249, 0.7)";
          } else if (foil === "rosegold" || foil === "#f472b6") {
            label.style.color = "#fbcfe8";
            label.style.textShadow = "0 1px 2px rgba(0,0,0,0.9), 0 0 10px rgba(251, 207, 232, 0.7)";
          } else if (foil === "frost" || foil.includes("255,255,255")) {
            label.style.color = "rgba(255,255,255,0.85)";
            label.style.textShadow = "0 1px 3px rgba(0,0,0,0.8)";
          } else {
            label.style.color = "#e6c88b";
            label.style.textShadow = "0 1px 2px rgba(0,0,0,0.9), 0 0 10px rgba(212, 175, 112, 0.7)";
          }
        }
      });
    }

    function addPersonalisedBottleToBag() {
      const input = document.getElementById("pers-engraving-input") || document.getElementById("personalise-input-field");
      const text = input ? input.value.trim() : "";
      const item = {
        id: `pers_${Date.now()}`,
        brand: activePersProduct.brand,
        name: activePersProduct.name,
        image: activePersProduct.image,
        concentration: activePersProduct.concentration,
        size: "100ml Grand",
        price: activePersProduct.price,
        engraving: text ? `${text.toUpperCase()} (${activePersFoil.toUpperCase()} FOIL)` : "ÉLIXORA FOREVER (GOLD LEAF FOIL)",
        qty: 1
      };
      cart.push(item);
      saveCart();
      showToast(`Added personalised ${item.name} to your bag`);
      openCartDrawer();
    }

    // 19. Discovery Sets & Scent Deals Adders
    function addDiscoverySetToBag(name, price, img) {
      const item = {
        id: `disc_${Date.now()}`,
        brand: "ÉLIXORA DISCOVERY",
        name: name,
        image: img || "/elixora_hero_bottle.jpg",
        concentration: "Discovery Vault (Includes 100% Cash-Back Voucher)",
        size: "6 x 10ml Luxury Vials",
        price: price,
        engraving: null,
        qty: 1
      };
      cart.push(item);
      saveCart();
      showToast(`Added ${name} to bag! ₹${price} coupon code included inside.`);
      openCartDrawer();
    }

    function addBundleToBag(bundleName, price, img) {
      const item = {
        id: `bundle_${Date.now()}`,
        brand: "SCENT COMBO ATELIER",
        name: bundleName,
        image: img || "/elixora_hero_bottle.jpg",
        concentration: "Special Scent Combo (50% Tropical Oil Formulation)",
        size: "Multi-Flacon Coffret",
        price: price,
        engraving: "Complimentary Laser Engraved Gift Box",
        qty: 1
      };
      cart.push(item);
      saveCart();
      showToast(`Added bundle "${bundleName}" to bag!`);
      openCartDrawer();
    }

    // 20. Store Locator & Appointment Booking
    function filterStoresByCity(city, btn) {
      document.querySelectorAll(".store-filter-btn").forEach(b => {
        if (b && b.classList) b.classList.remove("active");
      });
      if (btn && btn.classList) btn.classList.add("active");

      const cards = document.querySelectorAll(".store-card");
      cards.forEach(card => {
        if (city === "all" || card.getAttribute("data-city").toLowerCase().includes(city.toLowerCase())) {
          card.style.display = "flex";
        } else {
          card.style.display = "none";
        }
      });
    }

    function handleStoreSearch(val) {
      const query = val.toLowerCase().trim();
      const cards = document.querySelectorAll(".store-card");
      cards.forEach(card => {
        const text = card.textContent.toLowerCase();
        card.style.display = text.includes(query) ? "flex" : "none";
      });
    }

    function openBookStoreModal(storeName) {
      const modal = document.getElementById("book-store-modal");
      if (modal) modal.classList.add("active");
      const select = document.getElementById("booking-store-select");
      if (select && storeName) {
        for (let opt of select.options) {
          if (opt.value.toLowerCase().includes(storeName.toLowerCase()) || storeName.toLowerCase().includes(opt.value.toLowerCase())) {
            opt.selected = true;
            break;
          }
        }
      }
    }

    function closeBookStoreModal() {
      const modal = document.getElementById("book-store-modal");
      if (modal) modal.classList.remove("active");
    }

    function closeBookStoreModalOnBackdrop(e) {
      if (e.target.id === "book-store-modal") closeBookStoreModal();
    }

    function handleBookStoreSubmit(e) {
      e.preventDefault();
      const store = document.getElementById("booking-store-select").value;
      const date = document.getElementById("booking-date-input").value;
      const time = document.getElementById("booking-time-select").value;
      const name = document.getElementById("booking-guest-name").value;
      closeBookStoreModal();
      showToast(`Appointment confirmed for ${name} at ${store} on ${date} (${time})!`);
    }

    // 21. Corporate Gifting Calculator & Form
    function handleCorporateQty(qty) {
      const q = parseInt(qty, 10);
      const display = document.getElementById("corporate-qty-display");
      const totalDisplay = document.getElementById("corporate-total-calc");
      const perUnitDisplay = document.getElementById("corporate-per-unit");

      if (display) display.textContent = `${q} Units`;

      let baseRate = 2499;
      let discountRate = 0.20;
      if (q >= 250) {
        discountRate = 0.45;
      } else if (q >= 100) {
        discountRate = 0.30;
      }

      const effectiveRate = Math.round(baseRate * (1 - discountRate));
      const total = effectiveRate * q;

      if (totalDisplay) totalDisplay.textContent = `₹${total.toLocaleString("en-IN")}`;
      if (perUnitDisplay) perUnitDisplay.textContent = `₹${effectiveRate.toLocaleString("en-IN")} / bottle (${Math.round(discountRate * 100)}% bulk benefit)`;
    }

    function handleCorporateSubmit(e) {
      e.preventDefault();
      const name = document.getElementById("corp-name").value;
      const event = document.getElementById("corp-event").value;
      showToast(`Inquiry received for ${event}! Fragrance director will contact ${name} within 30 minutes.`);
      e.target.reset();
    }

    // 22. Track Order Modal
    function openTrackOrderModal() {
      const modal = document.getElementById("track-order-modal");
      if (modal) {
        modal.classList.add("active");
        modal.style.display = "flex";
      }
    }
    window.openTrackOrderModal = openTrackOrderModal;

    function closeTrackOrderModal() {
      const modal = document.getElementById("track-order-modal");
      if (modal) {
        modal.classList.remove("active");
        modal.style.display = "none";
      }
    }
    window.closeTrackOrderModal = closeTrackOrderModal;

    function closeTrackOrderModalOnBackdrop(e) {
      if (e.target.id === "track-order-modal") closeTrackOrderModal();
    }
    window.closeTrackOrderModalOnBackdrop = closeTrackOrderModalOnBackdrop;

    function handleTrackOrderSubmit(e) {
      e.preventDefault();
      const inputEl = document.getElementById("track-order-input");
      const inputVal = inputEl ? inputEl.value.trim() : "";
      const resultBox = document.getElementById("tracking-result-box");
      const awb = document.getElementById("track-awb-num");
      
      // Look up real status from Admin Database if exists
      let orderStatus = "Processing";
      let awbText = `BLUEDART-AIR-${inputVal || Math.floor(1000000 + Math.random() * 9000000)}`;
      
      const orders = getStoredOrders();
      const matchedOrder = orders.find(o => o.id.toLowerCase() === inputVal.toLowerCase() || (o.customer && o.customer.mobile.includes(inputVal)));
      if (matchedOrder) {
        orderStatus = matchedOrder.status;
        if (matchedOrder.awb) awbText = matchedOrder.awb;
      }

      if (resultBox) {
        resultBox.style.display = "block";
        if (awb) awb.textContent = awbText;

        // Dynamically adjust timeline based on actual order status
        const nodes = resultBox.querySelectorAll(".timeline-node");
        if (nodes && nodes.length >= 4) {
          // Reset
          nodes.forEach(n => n.classList.remove("complete", "active"));
          if (orderStatus === "Placed") {
            nodes[0].classList.add("complete");
            nodes[1].classList.add("active");
          } else if (orderStatus === "Processing") {
            nodes[0].classList.add("complete");
            nodes[1].classList.add("complete");
            nodes[2].classList.add("active");
          } else if (orderStatus === "Shipped") {
            nodes[0].classList.add("complete");
            nodes[1].classList.add("complete");
            nodes[2].classList.add("complete");
            nodes[3].classList.add("active");
          } else if (orderStatus === "Delivered") {
            nodes.forEach(n => n.classList.add("complete"));
          } else {
            nodes[0].classList.add("complete");
          }
        }

        showToast(matchedOrder ? `Found live order: ${matchedOrder.id} (${orderStatus})` : `Tracking status retrieved for ${inputVal || "order"}`);
      }
    }
    window.handleTrackOrderSubmit = handleTrackOrderSubmit;

    // 23. Toast System
    let toastTimeout = null;
    function showToast(msg) {
      const toast = document.getElementById("toast-notice");
      const text = document.getElementById("toast-text");
      text.textContent = msg;
      toast.classList.add("show");
      if (toastTimeout) clearTimeout(toastTimeout);
      toastTimeout = setTimeout(() => {
        toast.classList.remove("show");
      }, 3500);
    }

    function handleNewsletter(e) {
      e.preventDefault();
      showToast("Thank you. You are now initiated into the ÉLIXORA World.");
      e.target.reset();
    }

    // ==========================================================
    // 24. Interactive Side-by-Side Perfume Comparison Engine
    // ==========================================================
    function saveCompare() {
      localStorage.setItem("elixora_compare", JSON.stringify(compareList));
    }

    function toggleCompareProduct(productId, e) {
      if (e) {
        e.stopPropagation();
        e.preventDefault();
      }
      const prod = PRODUCTS.find(p => p.id === productId);
      if (!prod) return;

      const idx = compareList.indexOf(productId);
      if (idx > -1) {
        compareList.splice(idx, 1);
        showToast(`Removed ${prod.name} from comparison`);
      } else {
        if (compareList.length >= 2) {
          compareList[1] = productId;
          showToast(`Comparison updated with ${prod.name} (2/2)`);
        } else {
          compareList.push(productId);
          showToast(`Added ${prod.name} to comparison (${compareList.length}/2)`);
        }
      }

      saveCompare();
      updateCompareUI();
      renderCatalog();

      const modal = document.getElementById("compare-modal");
      if (modal && modal.classList.contains("active")) {
        renderCompareModalContent();
      }
    }

    function removeCompareItem(slotIndex) {
      if (slotIndex >= 0 && slotIndex < compareList.length) {
        const removedProd = PRODUCTS.find(p => p.id === compareList[slotIndex]);
        compareList.splice(slotIndex, 1);
        saveCompare();
        updateCompareUI();
        renderCatalog();
        showToast(`Removed ${removedProd ? removedProd.name : 'fragrance'} from comparison`);

        const modal = document.getElementById("compare-modal");
        if (modal && modal.classList.contains("active")) {
          renderCompareModalContent();
        }
      }
    }

    function clearComparison() {
      compareList = [];
      saveCompare();
      updateCompareUI();
      renderCatalog();
      showToast("Comparison cleared");
    }

    function updateCompareUI() {
      const count = compareList.length;
      const countBadge = document.getElementById("compare-count-badge");
      if (countBadge) countBadge.textContent = count;
      const mobileCount = document.getElementById("mobile-compare-count");
      if (mobileCount) mobileCount.textContent = count;
      const trayCount = document.getElementById("compare-tray-count");
      if (trayCount) trayCount.textContent = count;

      const tray = document.getElementById("floating-compare-tray");
      if (tray) {
        if (count > 0) {
          tray.classList.add("visible");
        } else {
          tray.classList.remove("visible");
        }
      }

      // Slot 1
      const slot1 = document.getElementById("compare-slot-1");
      if (slot1) {
        if (compareList[0]) {
          const p1 = PRODUCTS.find(p => p.id === compareList[0]);
          if (p1) {
            slot1.className = "compare-slot filled";
            slot1.innerHTML = `
              <img src="${p1.image}" alt="${p1.name}" class="compare-slot-thumb" />
              <div class="compare-slot-info">
                <span class="compare-slot-name">${p1.name}</span>
                <span class="compare-slot-conc">₹${p1.price.toLocaleString("en-IN")} &middot; ${p1.concentration}</span>
              </div>
              <button class="compare-slot-remove" onclick="removeCompareItem(0)" title="Remove">&times;</button>
            `;
          }
        } else {
          slot1.className = "compare-slot";
          slot1.innerHTML = `<span class="compare-slot-placeholder">+ Select 1st Perfume</span>`;
        }
      }

      // Slot 2
      const slot2 = document.getElementById("compare-slot-2");
      if (slot2) {
        if (compareList[1]) {
          const p2 = PRODUCTS.find(p => p.id === compareList[1]);
          if (p2) {
            slot2.className = "compare-slot filled";
            slot2.innerHTML = `
              <img src="${p2.image}" alt="${p2.name}" class="compare-slot-thumb" />
              <div class="compare-slot-info">
                <span class="compare-slot-name">${p2.name}</span>
                <span class="compare-slot-conc">₹${p2.price.toLocaleString("en-IN")} &middot; ${p2.concentration}</span>
              </div>
              <button class="compare-slot-remove" onclick="removeCompareItem(1)" title="Remove">&times;</button>
            `;
          }
        } else {
          slot2.className = "compare-slot";
          slot2.innerHTML = `<span class="compare-slot-placeholder">+ Select 2nd Perfume</span>`;
        }
      }
    }

    function addActiveModalToCompare() {
      if (!activeModalProduct) return;
      toggleCompareProduct(activeModalProduct.id);
      closeProductModal();
      if (compareList.length === 2) {
        openCompareModal();
      }
    }

    function openCompareModal() {
      // Default to premier fragrances if list is empty for instant comparison
      if (compareList.length === 0) {
        compareList = ["p1", "p3"];
        saveCompare();
        updateCompareUI();
        renderCatalog();
      } else if (compareList.length === 1) {
        const alt = PRODUCTS.find(p => p.id !== compareList[0]);
        if (alt) {
          compareList.push(alt.id);
          saveCompare();
          updateCompareUI();
          renderCatalog();
        }
      }

      populateCompareDropdowns();
      renderCompareModalContent();

      const modal = document.getElementById("compare-modal");
      if (modal) {
        modal.classList.add("active");
        document.body.style.overflow = "hidden";
      }
    }

    function closeCompareModal() {
      const modal = document.getElementById("compare-modal");
      if (modal) {
        modal.classList.remove("active");
        document.body.style.overflow = "";
      }
    }

    function closeCompareModalOnBackdrop(e) {
      if (e.target.id === "compare-modal") {
        closeCompareModal();
      }
    }

    function populateCompareDropdowns() {
      const selA = document.getElementById("compare-select-a");
      const selB = document.getElementById("compare-select-b");
      if (!selA || !selB) return;

      const options = PRODUCTS.map(p => `
        <option value="${p.id}">${p.name} (${p.concentration} &middot; ₹${p.price.toLocaleString("en-IN")})</option>
      `).join("");

      selA.innerHTML = options;
      selB.innerHTML = options;

      if (compareList[0]) selA.value = compareList[0];
      if (compareList[1]) selB.value = compareList[1];
    }

    function handleCompareDropdownChange(slot, newProductId) {
      compareList[slot] = newProductId;
      saveCompare();
      updateCompareUI();
      renderCatalog();
      renderCompareModalContent();
    }

    function swapCompareItems() {
      if (compareList.length >= 2) {
        const temp = compareList[0];
        compareList[0] = compareList[1];
        compareList[1] = temp;
        saveCompare();
        updateCompareUI();

        const selA = document.getElementById("compare-select-a");
        const selB = document.getElementById("compare-select-b");
        if (selA) selA.value = compareList[0];
        if (selB) selB.value = compareList[1];

        renderCompareModalContent();
      }
    }

    function openPersonaliseForProduct(productName) {
      closeCompareModal();
      handlePersonalisePerfumeSelect(productName);
      const persSelect = document.getElementById("pers-perfume-select");
      if (persSelect) persSelect.value = productName;
      const persSection = document.getElementById("personalise");
      if (persSection) {
        persSection.scrollIntoView({ behavior: "smooth" });
      }
    }

    // Helper to extract key notes vocabulary
    function extractProductNoteKeywords(product) {
      const fullText = `${product.topNotes} ${product.heartNotes} ${product.baseNotes}`.toLowerCase();
      const dictionary = [
        "oud", "amber", "rose", "bergamot", "tonka", "musk", "iris", "pepper",
        "cedar", "jasmine", "sandalwood", "patchouli", "vetiver", "incense",
        "cardamom", "leather", "saffron", "neroli", "tuberose", "coffee",
        "peach", "grapefruit", "mint", "lavender", "cinnamon", "tobacco",
        "ambergris", "violet", "oakmoss", "marine", "salt", "pear", "freesia"
      ];
      return dictionary.filter(w => fullText.includes(w));
    }

    function renderComparativeNotePills(notesText, sharedKeywords) {
      const notesArray = notesText.split(/[·•,]/).map(s => s.trim()).filter(Boolean);
      return notesArray.map(item => {
        const isShared = sharedKeywords.some(kw => item.toLowerCase().includes(kw));
        return `<span class="note-pill-tag ${isShared ? 'shared' : ''}" title="${isShared ? 'Shared accord with compared perfume' : ''}">${isShared ? '✦ ' : ''}${item}</span>`;
      }).join("");
    }

    function getConcentrationProfile(concStr) {
      const upper = (concStr || "").toUpperCase();
      if (upper.includes("EXTRAIT")) {
        return {
          label: "Extrait de Parfum",
          oilPercent: "50% Pure Tropical Oil",
          gauge: 98,
          sillage: "Room-filling &amp; Beast Mode",
          longevity: "24h+ On Skin &amp; Fabric",
          tag: "Extrait (50% Oil)"
        };
      } else if (upper.includes("PARFUM")) {
        return {
          label: "Pure Parfum",
          oilPercent: "35% Botanical Essence Oil",
          gauge: 84,
          sillage: "Strong &amp; Intoxicating Projection",
          longevity: "14&ndash;18 Hours Sustained",
          tag: "Parfum (35% Oil)"
        };
      } else if (upper.includes("EDP") || upper.includes("EAU DE PARFUM")) {
        return {
          label: "Eau de Parfum",
          oilPercent: "25% Essence Oil Blend",
          gauge: 72,
          sillage: "Moderate to Heavy Presence",
          longevity: "10&ndash;12 Hours Continuous",
          tag: "EDP (25% Oil)"
        };
      } else {
        return {
          label: "Eau de Toilette",
          oilPercent: "15% Light Essence",
          gauge: 52,
          sillage: "Intimate Crisp Aura",
          longevity: "6&ndash;8 Hours Duration",
          tag: "EDT (15% Oil)"
        };
      }
    }

    function renderCompareModalContent() {
      const grid = document.getElementById("compare-grid-content");
      if (!grid) return;

      const p1 = PRODUCTS.find(p => p.id === compareList[0]) || PRODUCTS[0];
      const p2 = PRODUCTS.find(p => p.id === compareList[1]) || PRODUCTS[1];

      // Update dropdown inputs to reflect current items
      const selA = document.getElementById("compare-select-a");
      const selB = document.getElementById("compare-select-b");
      if (selA) selA.value = p1.id;
      if (selB) selB.value = p2.id;

      // Note keyword analysis
      const notesA = extractProductNoteKeywords(p1);
      const notesB = extractProductNoteKeywords(p2);
      const sharedNotes = notesA.filter(k => notesB.includes(k));

      // Concentration metrics
      const conc1 = getConcentrationProfile(p1.concentration);
      const conc2 = getConcentrationProfile(p2.concentration);

      // Price & value analysis
      const diffPrice = Math.abs(p1.price - p2.price);
      const unitA = Math.round(p1.price / 100);
      const unitB = Math.round(p2.price / 100);

      const deltaTagA = p1.price < p2.price 
        ? `<span class="compare-price-delta cheaper">&#10003; Save ₹${diffPrice.toLocaleString("en-IN")}</span>`
        : (p1.price > p2.price ? `<span class="compare-price-delta higher">+₹${diffPrice.toLocaleString("en-IN")} Tier</span>` : `<span class="compare-price-delta">Equal Price</span>`);

      const deltaTagB = p2.price < p1.price 
        ? `<span class="compare-price-delta cheaper">&#10003; Save ₹${diffPrice.toLocaleString("en-IN")}</span>`
        : (p2.price > p1.price ? `<span class="compare-price-delta higher">+₹${diffPrice.toLocaleString("en-IN")} Tier</span>` : `<span class="compare-price-delta">Equal Price</span>`);

      // Shared Accord Insights Banner
      let sharedAccordsHTML = "";
      if (sharedNotes.length > 0) {
        sharedAccordsHTML = `
          <div class="compare-shared-accords-box">
            <div class="shared-accords-title">
              <span style="font-size: 1.15rem; color: var(--gold);">&#10022;</span>
              <span>Harmonizing Shared Accords (${sharedNotes.length} in common)</span>
            </div>
            <div class="shared-accords-pills">
              ${sharedNotes.map(n => `<span class="note-pill-tag shared">&#10022; ${n.toUpperCase()}</span>`).join("")}
            </div>
            <p style="width: 100%; font-size: 0.8rem; color: var(--muted-color); margin: 4px 0 0 0; line-height: 1.6;">
              Both fragrances share <strong>${sharedNotes.map(s => s.charAt(0).toUpperCase() + s.slice(1)).join(", ")}</strong> chords. You can layer both formulas together for a multifaceted signature sillage, or alternate them between daytime and gala wear.
            </p>
          </div>
        `;
      } else {
        sharedAccordsHTML = `
          <div class="compare-shared-accords-box">
            <div class="shared-accords-title">
              <span style="font-size: 1.15rem; color: var(--gold);">&#10022;</span>
              <span>Contrasting Olfactory Architecture</span>
            </div>
            <p style="width: 100%; font-size: 0.8rem; color: var(--muted-color); margin: 0; line-height: 1.6;">
              <strong>${p1.name}</strong> (${p1.category}) and <strong>${p2.name}</strong> (${p2.category}) present entirely distinct scent families with zero accord overlap, making them an ideal two-bottle wardrobe pairing for contrasting moods and seasons.
            </p>
          </div>
        `;
      }

      grid.innerHTML = `
        ${sharedAccordsHTML}

        <!-- Fragrance A Column -->
        <div class="compare-column">
          <div class="compare-flacon-stage">
            <img src="${p1.image}" alt="${p1.name}" class="compare-flacon-img" />
          </div>

          <div>
            <span class="compare-brand-tag">${p1.brand}</span>
            <h3 class="compare-prod-name">${p1.name}</h3>
            <div>
              <span class="compare-family-badge">${p1.category} &middot; ${p1.gender}</span>
              <span style="color: var(--gold); font-size: 0.82rem; margin-left: 8px;">&#9733;&#9733;&#9733;&#9733;&#9733; 5.0</span>
            </div>
            <p style="font-size: 0.84rem; color: var(--muted-color); line-height: 1.6; margin-top: 8px;">
              ${p1.description}
            </p>
          </div>

          <!-- Price & Value Comparison Box -->
          <div class="compare-metric-box">
            <div class="compare-metric-title">
              <span>Price &amp; Volume Metrics</span>
              <span>100ml Master Flacon</span>
            </div>
            <div style="display: flex; align-items: baseline; gap: 8px;">
              <span class="compare-price-val">₹${p1.price.toLocaleString("en-IN")}</span>
              ${deltaTagA}
            </div>
            <div class="compare-unit-price">
              Equivalent to ₹${unitA} / ml &middot; Sizes: ${p1.sizes.join(", ")}
            </div>
            <div style="font-size: 0.72rem; color: var(--gold); margin-top: 6px;">
              &#10003; Complimentary Laser Engraving &middot; Free BlueDart Priority Air
            </div>
          </div>

          <!-- Concentration & Sillage Comparison Box -->
          <div class="compare-metric-box">
            <div class="compare-metric-title">
              <span>Formula Concentration &amp; Longevity</span>
              <span style="color: #fff;">${conc1.tag}</span>
            </div>
            <div style="font-weight: 600; color: var(--gold-light); font-size: 0.88rem;">
              ${conc1.oilPercent}
            </div>
            <div class="compare-bar-track">
              <div class="compare-bar-fill" style="width: ${conc1.gauge}%;"></div>
            </div>
            <div class="compare-bar-meta">
              <span>Longevity: ${conc1.longevity}</span>
              <span>${conc1.gauge}% Density</span>
            </div>
            <div style="font-size: 0.74rem; color: var(--muted-color); margin-top: 6px;">
              <strong>Sillage:</strong> ${conc1.sillage}
            </div>
          </div>

          <!-- Olfactory Notes Breakdown Box -->
          <div class="compare-metric-box">
            <div class="compare-metric-title">
              <span>Olfactory Pyramid &amp; Notes</span>
              <span style="font-size: 0.68rem; color: var(--gold);">&#10022; Highlighted = Shared</span>
            </div>

            <div class="compare-notes-tier">
              <div class="compare-tier-heading">Top Notes</div>
              <div class="compare-notes-pills">
                ${renderComparativeNotePills(p1.topNotes, sharedNotes)}
              </div>
            </div>

            <div class="compare-notes-tier">
              <div class="compare-tier-heading">Heart Notes</div>
              <div class="compare-notes-pills">
                ${renderComparativeNotePills(p1.heartNotes, sharedNotes)}
              </div>
            </div>

            <div class="compare-notes-tier">
              <div class="compare-tier-heading">Base Notes</div>
              <div class="compare-notes-pills">
                ${renderComparativeNotePills(p1.baseNotes, sharedNotes)}
              </div>
            </div>
          </div>

          <!-- Context & Wear Recommendation -->
          <div class="compare-metric-box">
            <div class="compare-metric-title">
              <span>Styling &amp; Occasion Profile</span>
            </div>
            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
              <span class="note-pill-tag">Season: ${p1.season.toUpperCase()}</span>
              <span class="note-pill-tag">Occasion: ${p1.occasion}</span>
              <span class="note-pill-tag">Glass: Crystal Flacon</span>
            </div>
          </div>

          <div class="compare-actions-col">
            <button class="compare-add-btn" onclick="addToCart('${p1.id}', '${p1.concentration}', '100ml', ${p1.price}); closeCompareModal(); openCartDrawer();">
              Add ${p1.name} to Bag &middot; ₹${p1.price.toLocaleString("en-IN")}
            </button>
            <button class="compare-engrave-btn" onclick="openPersonaliseForProduct('${p1.name}')">
              ✦ Custom Engrave ${p1.name}
            </button>
          </div>
        </div>

        <!-- Fragrance B Column -->
        <div class="compare-column">
          <div class="compare-flacon-stage">
            <img src="${p2.image}" alt="${p2.name}" class="compare-flacon-img" />
          </div>

          <div>
            <span class="compare-brand-tag">${p2.brand}</span>
            <h3 class="compare-prod-name">${p2.name}</h3>
            <div>
              <span class="compare-family-badge">${p2.category} &middot; ${p2.gender}</span>
              <span style="color: var(--gold); font-size: 0.82rem; margin-left: 8px;">&#9733;&#9733;&#9733;&#9733;&#9733; 5.0</span>
            </div>
            <p style="font-size: 0.84rem; color: var(--muted-color); line-height: 1.6; margin-top: 8px;">
              ${p2.description}
            </p>
          </div>

          <!-- Price & Value Comparison Box -->
          <div class="compare-metric-box">
            <div class="compare-metric-title">
              <span>Price &amp; Volume Metrics</span>
              <span>100ml Master Flacon</span>
            </div>
            <div style="display: flex; align-items: baseline; gap: 8px;">
              <span class="compare-price-val">₹${p2.price.toLocaleString("en-IN")}</span>
              ${deltaTagB}
            </div>
            <div class="compare-unit-price">
              Equivalent to ₹${unitB} / ml &middot; Sizes: ${p2.sizes.join(", ")}
            </div>
            <div style="font-size: 0.72rem; color: var(--gold); margin-top: 6px;">
              &#10003; Complimentary Laser Engraving &middot; Free BlueDart Priority Air
            </div>
          </div>

          <!-- Concentration & Sillage Comparison Box -->
          <div class="compare-metric-box">
            <div class="compare-metric-title">
              <span>Formula Concentration &amp; Longevity</span>
              <span style="color: #fff;">${conc2.tag}</span>
            </div>
            <div style="font-weight: 600; color: var(--gold-light); font-size: 0.88rem;">
              ${conc2.oilPercent}
            </div>
            <div class="compare-bar-track">
              <div class="compare-bar-fill" style="width: ${conc2.gauge}%;"></div>
            </div>
            <div class="compare-bar-meta">
              <span>Longevity: ${conc2.longevity}</span>
              <span>${conc2.gauge}% Density</span>
            </div>
            <div style="font-size: 0.74rem; color: var(--muted-color); margin-top: 6px;">
              <strong>Sillage:</strong> ${conc2.sillage}
            </div>
          </div>

          <!-- Olfactory Notes Breakdown Box -->
          <div class="compare-metric-box">
            <div class="compare-metric-title">
              <span>Olfactory Pyramid &amp; Notes</span>
              <span style="font-size: 0.68rem; color: var(--gold);">&#10022; Highlighted = Shared</span>
            </div>

            <div class="compare-notes-tier">
              <div class="compare-tier-heading">Top Notes</div>
              <div class="compare-notes-pills">
                ${renderComparativeNotePills(p2.topNotes, sharedNotes)}
              </div>
            </div>

            <div class="compare-notes-tier">
              <div class="compare-tier-heading">Heart Notes</div>
              <div class="compare-notes-pills">
                ${renderComparativeNotePills(p2.heartNotes, sharedNotes)}
              </div>
            </div>

            <div class="compare-notes-tier">
              <div class="compare-tier-heading">Base Notes</div>
              <div class="compare-notes-pills">
                ${renderComparativeNotePills(p2.baseNotes, sharedNotes)}
              </div>
            </div>
          </div>

          <!-- Context & Wear Recommendation -->
          <div class="compare-metric-box">
            <div class="compare-metric-title">
              <span>Styling &amp; Occasion Profile</span>
            </div>
            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
              <span class="note-pill-tag">Season: ${p2.season.toUpperCase()}</span>
              <span class="note-pill-tag">Occasion: ${p2.occasion}</span>
              <span class="note-pill-tag">Glass: Crystal Flacon</span>
            </div>
          </div>

          <div class="compare-actions-col">
            <button class="compare-add-btn" onclick="addToCart('${p2.id}', '${p2.concentration}', '100ml', ${p2.price}); closeCompareModal(); openCartDrawer();">
              Add ${p2.name} to Bag &middot; ₹${p2.price.toLocaleString("en-IN")}
            </button>
            <button class="compare-engrave-btn" onclick="openPersonaliseForProduct('${p2.name}')">
              ✦ Custom Engrave ${p2.name}
            </button>
          </div>
        </div>
      `;
    }

    // 25. Mobile Menu
    const mobileBtn = document.getElementById("mobile-menu-btn");
    const mobileOverlay = document.getElementById("mobile-nav-overlay");
    const mobilePanel = document.getElementById("mobile-nav-panel");
    const closeMobileBtn = document.getElementById("close-mobile-menu-btn");

    function toggleMobileMenu(open) {
      mobileOverlay.classList.toggle("active", open);
      mobilePanel.style.transform = open ? "translateX(0)" : "translateX(-100%)";
    }

    function closeMobileMenu() {
      toggleMobileMenu(false);
    }

    if (mobileBtn) {
      mobileBtn.addEventListener("click", () => toggleMobileMenu(true));
    }
    if (closeMobileBtn) {
      closeMobileBtn.addEventListener("click", () => toggleMobileMenu(false));
    }
    if (mobileOverlay) {
      mobileOverlay.addEventListener("click", () => toggleMobileMenu(false));
    }
    document.querySelectorAll(".mobile-nav-link").forEach(l => {
      l.addEventListener("click", () => toggleMobileMenu(false));
    });

    // 25.b Collection Cards GSAP Sophisticated Hover Animation
    function initCollectionCardHoverAnimations() {
      if (!window.gsap) return;

      const cards = document.querySelectorAll(".collection-card");
      cards.forEach(card => {
        const bgImg = card.querySelector(".collection-bg-img");
        const content = card.querySelector(".collection-content");
        const extraDetails = card.querySelector(".collection-extra-details");
        const pills = card.querySelectorAll(".collection-note-pill");
        const overlay = card.querySelector(".collection-overlay");

        if (!bgImg || !content) return;

        // Ensure smooth rendering
        gsap.set(bgImg, { scale: 1, filter: "brightness(0.62) saturate(0.95)" });
        gsap.set(content, { y: 0 });
        if (extraDetails) {
          gsap.set(extraDetails, { height: 0, opacity: 0 });
        }

        // Create individual timeline paused
        const hoverTl = gsap.timeline({ paused: true });

        // Gentle zoom and atmospheric brightening of the luxury bottle image
        hoverTl.to(bgImg, {
          scale: 1.12,
          filter: "brightness(0.78) saturate(1.1)",
          duration: 0.85,
          ease: "power2.out"
        }, 0);

        // Subtly enhance gradient overlay
        if (overlay) {
          hoverTl.to(overlay, {
            opacity: 0.96,
            duration: 0.7,
            ease: "power2.out"
          }, 0);
        }

        // Shift the product text block upwards gently to make room for reveals
        hoverTl.to(content, {
          y: -14,
          duration: 0.75,
          ease: "power3.out"
        }, 0);

        // Smoothly reveal extra origin & intensity metadata
        if (extraDetails) {
          hoverTl.to(extraDetails, {
            height: "auto",
            opacity: 1,
            duration: 0.6,
            ease: "power2.out"
          }, 0.1);
        }

        // Animate notes pills with a subtle glow & stagger
        if (pills && pills.length) {
          hoverTl.to(pills, {
            backgroundColor: "rgba(212, 175, 112, 0.16)",
            borderColor: "rgba(212, 175, 112, 0.4)",
            color: "#ffffff",
            stagger: 0.04,
            duration: 0.5,
            ease: "power2.out"
          }, 0.08);
        }

        // Lift card boundary subtly
        hoverTl.to(card, {
          borderColor: "rgba(212, 175, 112, 0.55)",
          boxShadow: "0 28px 60px rgba(0, 0, 0, 0.65), 0 0 25px rgba(212, 175, 112, 0.12)",
          duration: 0.6,
          ease: "power2.out"
        }, 0);

        // Event listeners with GSAP timeline play/reverse
        card.addEventListener("mouseenter", () => {
          hoverTl.play();
        });

        card.addEventListener("mouseleave", () => {
          hoverTl.reverse();
        });
      });
    }

    // 25b. GSAP ScrollTrigger Animations for Fragrance Collections & Editorial Story
    function initScrollAnimations() {
      if (window.gsap && window.ScrollTrigger) {
        gsap.registerPlugin(window.ScrollTrigger);

        // 1. Fragrance Collections (Explore By Fragrance)
        gsap.from("#collections .section-header", {
          scrollTrigger: {
            trigger: "#collections",
            start: "top 80%",
            toggleActions: "play none none reverse"
          },
          opacity: 0,
          y: 35,
          duration: 1.2,
          ease: "power2.out"
        });

        gsap.from("#collections .collection-card", {
          scrollTrigger: {
            trigger: "#collections .collections-grid",
            start: "top 85%",
            toggleActions: "play none none reverse"
          },
          opacity: 0,
          y: 55,
          duration: 1.1,
          stagger: 0.15,
          ease: "power2.out"
        });

        // 2. Editorial Story Elements (Our Philosophy)
        gsap.from("#story .story-img-frame", {
          scrollTrigger: {
            trigger: "#story",
            start: "top 75%",
            toggleActions: "play none none reverse"
          },
          opacity: 0,
          scale: 0.94,
          duration: 1.4,
          ease: "power3.out"
        });

        gsap.from("#story .story-content > *", {
          scrollTrigger: {
            trigger: "#story .story-content",
            start: "top 80%",
            toggleActions: "play none none reverse"
          },
          opacity: 0,
          y: 35,
          duration: 1.1,
          stagger: 0.15,
          ease: "power2.out"
        });

        // 3. Haute Parfumerie (The Collection) header fade-in
        gsap.from("#catalog .section-header", {
          scrollTrigger: {
            trigger: "#catalog",
            start: "top 80%",
            toggleActions: "play none none reverse"
          },
          opacity: 0,
          y: 30,
          duration: 1.2,
          ease: "power2.out"
        });

        // 4. Discovery Sets header fade-in
        gsap.from("#discovery .section-header", {
          scrollTrigger: {
            trigger: "#discovery",
            start: "top 80%",
            toggleActions: "play none none reverse"
          },
          opacity: 0,
          y: 30,
          duration: 1.2,
          ease: "power2.out"
        });
      }
    }

    // 26. Initial Entrance Animation & Seeds (GSAP Timeline)
    window.addEventListener("DOMContentLoaded", () => {
      renderCatalog();
      renderSeasonalSection("autumn");
      updateCartUI();
      updateWishlistUI();
      updateCompareUI();
      setupCursorInteractions();
      initCollectionCardHoverAnimations();
      initHeroPerfumeCarousel();
      initScrollAnimations();

      // Universal Smooth Anchor Navigation (prevents hash jumps to top/homepage)
      document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
          const href = this.getAttribute('href');
          if (href === '#' || !href) {
            e.preventDefault();
            return;
          }
          if (href === '#admin') {
            e.preventDefault();
            openAdminLoginModal();
            return;
          }
          const target = document.querySelector(href);
          if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth' });
          }
        });
      });

      // Check admin hash on initial mount
      if (window.location.hash.toLowerCase() === "#admin") {
        setTimeout(openAdminLoginModal, 300);
      }

      // Seed MYOP & Personalisation modules
      updateStudioVisualizer();
      handlePersonalisePerfumeSelect("Noir Intense");
      handleCorporateQty(100);

      // Pre-fill today's date in booking modal
      const today = new Date().toISOString().split("T")[0];
      const dateInput = document.getElementById("booking-date-input");
      if (dateInput) dateInput.value = today;

      if (window.gsap) {
        const tl = gsap.timeline();
        tl.from("#main-header", {
          y: -40,
          opacity: 0,
          duration: 1,
          ease: "power3.out"
        })
        .from(".hero-left .eyebrow", {
          opacity: 0,
          x: -30,
          duration: 0.8,
          ease: "power2.out"
        }, "-=0.6")
        .from(".hero-heading", {
          opacity: 0,
          y: 40,
          duration: 1.1,
          ease: "power3.out"
        }, "-=0.6")
        .from(".hero-tagline", {
          opacity: 0,
          y: 20,
          duration: 0.8,
          ease: "power2.out"
        }, "-=0.7")
        .from(".hero-actions", {
          opacity: 0,
          y: 20,
          duration: 0.8,
          ease: "power2.out"
        }, "-=0.6")
        .from("#hero-perfume-carousel-wrap", {
          scale: 1.06,
          opacity: 0,
          duration: 1.6,
          ease: "power2.out"
        }, "-=1.0")
        .from(".hero-carousel-controls-bar", {
          opacity: 0,
          y: 15,
          duration: 0.8
        }, "-=0.5");
      }
    });
  
    // ==========================================================
    // 25. ADMIN PORTAL & LIVE ORDER MANAGEMENT SYSTEM
    // ==========================================================
    const DEFAULT_ADMIN_PIN = "0609";
    let adminActiveFilter = "all";
    let adminSearchQuery = "";

    // Mock initial orders if fresh system
    function getStoredOrders() {
      let orders = localStorage.getItem("elixora_orders");
      if (!orders) {
        orders = [
          {
            id: "ELX-918234",
            date: new Date(Date.now() - 3600000 * 26).toLocaleString("en-IN", { dateStyle: "medium", timeStyle: "short" }),
            customer: {
              name: "Ananya Singhania",
              mobile: "+91 98201 44512",
              email: "ananya.singhania@luxurymail.com"
            },
            address: {
              street: "Penthouse 42B, Altamount Road",
              city: "Mumbai",
              state: "Maharashtra",
              pincode: "400026"
            },
            items: [
              { name: "Golden Elixir", size: "100ml", qty: 1, price: 14999 }
            ],
            paymentMethod: "UPI",
            total: 14999,
            status: "Delivered",
            awb: "BLUEDART-AIR-7829104"
          },
          {
            id: "ELX-847291",
            date: new Date(Date.now() - 3600000 * 5).toLocaleString("en-IN", { dateStyle: "medium", timeStyle: "short" }),
            customer: {
              name: "Vikramaditya Roy",
              mobile: "+91 98110 52390",
              email: "vikram.roy@atelierholdings.com"
            },
            address: {
              street: "Villa 14, Amrita Shergill Marg",
              city: "New Delhi",
              state: "Delhi",
              pincode: "110003"
            },
            items: [
              { name: "Midnight Oud", size: "150ml", qty: 1, price: 18999 },
              { name: "Ivory Musk", size: "50ml", qty: 2, price: 9999 }
            ],
            paymentMethod: "Card",
            total: 38997,
            status: "Shipped",
            awb: "BLUEDART-AIR-3918205"
          }
        ];
        localStorage.setItem("elixora_orders", JSON.stringify(orders));
      } else {
        try {
          orders = JSON.parse(orders);
        } catch (e) {
          orders = [];
        }
      }
      return orders;
    }

    function saveStoredOrders(orders) {
      localStorage.setItem("elixora_orders", JSON.stringify(orders));
    }

    function openAdminLoginModal() {
      if (sessionStorage.getItem("elixora_admin_logged") === "true") {
        openAdminPortal();
        return;
      }
      const modal = document.getElementById("admin-login-modal");
      if (modal) {
        modal.classList.add("active");
        modal.style.display = "flex";
        modal.style.opacity = "1";
        modal.style.pointerEvents = "all";
        const pinInput = document.getElementById("admin-pin-input");
        if (pinInput) {
          pinInput.value = "";
          setTimeout(() => pinInput.focus(), 150);
        }
      }
    }
    window.openAdminLoginModal = openAdminLoginModal;

    function closeAdminLoginModal() {
      const modal = document.getElementById("admin-login-modal");
      if (modal) {
        modal.classList.remove("active");
        modal.style.display = "none";
      }
    }
    window.closeAdminLoginModal = closeAdminLoginModal;

    function closeAdminLoginOnBackdrop(e) {
      if (e.target.id === "admin-login-modal") closeAdminLoginModal();
    }
    window.closeAdminLoginOnBackdrop = closeAdminLoginOnBackdrop;

    function handleAdminLogin(e) {
      e.preventDefault();
      const pin = document.getElementById("admin-pin-input").value.trim();
      const err = document.getElementById("admin-login-err");
      if (pin === DEFAULT_ADMIN_PIN) {
        sessionStorage.setItem("elixora_admin_logged", "true");
        err.style.display = "none";
        closeAdminLoginModal();
        openAdminPortal();
      } else {
        err.style.display = "block";
      }
    }
    window.handleAdminLogin = handleAdminLogin;

    function handleAdminLogout() {
      sessionStorage.removeItem("elixora_admin_logged");
      closeAdminPortal();
      showToast("Admin session locked.");
    }
    window.handleAdminLogout = handleAdminLogout;

    function openAdminPortal() {
      const portal = document.getElementById("admin-portal");
      if (portal) {
        portal.classList.add("active");
        portal.style.display = "flex";
        renderAdminDashboard();
        window.location.hash = "admin";
      }
    }
    window.openAdminPortal = openAdminPortal;

    function closeAdminPortal() {
      const portal = document.getElementById("admin-portal");
      if (portal) {
        portal.classList.remove("active");
        if (window.location.hash === "#admin") {
          history.pushState("", document.title, window.location.pathname + window.location.search);
        }
      }
    }
    window.closeAdminPortal = closeAdminPortal;

    function filterAdminOrders(status, btn) {
      adminActiveFilter = status;
      document.querySelectorAll(".admin-filter-btn").forEach(b => b.classList.remove("active"));
      if (btn) btn.classList.add("active");
      renderAdminOrdersTable();
    }
    window.filterAdminOrders = filterAdminOrders;

    function handleAdminOrderSearch(val) {
      adminSearchQuery = val.toLowerCase().trim();
      renderAdminOrdersTable();
    }
    window.handleAdminOrderSearch = handleAdminOrderSearch;

    function updateOrderStatus(orderId, newStatus) {
      const orders = getStoredOrders();
      const order = orders.find(o => o.id === orderId);
      if (order) {
        order.status = newStatus;
        if (newStatus === "Shipped" && !order.awb) {
          order.awb = `BLUEDART-AIR-${Math.floor(1000000 + Math.random() * 9000000)}`;
        }
        saveStoredOrders(orders);
        renderAdminDashboard();
        showToast(`Order ${orderId} updated to ${newStatus}`);
      }
    }
    window.updateOrderStatus = updateOrderStatus;

    function renderAdminDashboard() {
      const orders = getStoredOrders();

      // Stats
      const totalOrders = orders.length;
      const totalRev = orders.reduce((sum, o) => sum + (Number(o.total) || 0), 0);
      const pendingOrders = orders.filter(o => o.status === "Placed" || o.status === "Processing").length;
      const shippedOrders = orders.filter(o => o.status === "Shipped").length;
      const deliveredOrders = orders.filter(o => o.status === "Delivered").length;

      document.getElementById("admin-stat-total-orders").textContent = totalOrders;
      document.getElementById("admin-stat-total-rev").textContent = "₹" + totalRev.toLocaleString("en-IN");
      document.getElementById("admin-stat-pending-orders").textContent = pendingOrders;
      document.getElementById("admin-stat-shipped-orders").textContent = shippedOrders;
      document.getElementById("admin-stat-delivered-orders").textContent = deliveredOrders;

      // Filter Counts
      document.getElementById("count-all").textContent = totalOrders;
      document.getElementById("count-placed").textContent = orders.filter(o => o.status === "Placed").length;
      document.getElementById("count-processing").textContent = orders.filter(o => o.status === "Processing").length;
      document.getElementById("count-shipped").textContent = shippedOrders;
      document.getElementById("count-delivered").textContent = deliveredOrders;
      document.getElementById("count-cancelled").textContent = orders.filter(o => o.status === "Cancelled").length;

      renderAdminOrdersTable();
    }

    function renderAdminOrdersTable() {
      const orders = getStoredOrders();
      const tbody = document.getElementById("admin-orders-tbody");
      const emptyState = document.getElementById("admin-empty-state");
      if (!tbody) return;

      let filtered = orders;
      if (adminActiveFilter !== "all") {
        filtered = filtered.filter(o => o.status === adminActiveFilter);
      }

      if (adminSearchQuery) {
        filtered = filtered.filter(o => {
          const matchId = (o.id || "").toLowerCase().includes(adminSearchQuery);
          const matchName = (o.customer && o.customer.name ? o.customer.name.toLowerCase() : "").includes(adminSearchQuery);
          const matchPhone = (o.customer && o.customer.mobile ? o.customer.mobile.toLowerCase() : "").includes(adminSearchQuery);
          return matchId || matchName || matchPhone;
        });
      }

      if (filtered.length === 0) {
        tbody.innerHTML = "";
        emptyState.style.display = "block";
        return;
      }

      emptyState.style.display = "none";
      tbody.innerHTML = "";
      filtered.forEach(order => {
        const badgeClass = {
          "Placed": "badge-placed",
          "Processing": "badge-processing",
          "Shipped": "badge-shipped",
          "Delivered": "badge-delivered",
          "Cancelled": "badge-cancelled"
        }[order.status] || "badge-placed";

        const itemsHtml = (order.items || []).map(it => 
          `<div style="font-size: 0.78rem; line-height: 1.4;">${it.qty}x <strong>${it.name}</strong> (${it.size || "100ml"})</div>`
        ).join("");

        const tr = document.createElement("tr");
        tr.innerHTML = `
          <td>
            <strong style="color: var(--gold-light); font-family: monospace; font-size: 0.88rem;">${order.id}</strong>
            <div style="color: var(--muted-color); font-size: 0.72rem; margin-top: 3px;">${order.date || "Just now"}</div>
            ${order.awb ? `<div style="font-size: 0.68rem; color: #a78bfa; margin-top: 2px;">${order.awb}</div>` : ""}
          </td>
          <td>
            <div style="font-weight: 600; color: #fff;">${order.customer?.name || "VIP Guest"}</div>
            <div style="color: var(--muted-color); font-size: 0.75rem;">${order.customer?.mobile || "—"}</div>
            <div style="color: var(--muted-color); font-size: 0.72rem;">${order.customer?.email || "—"}</div>
          </td>
          <td>
            <div style="font-size: 0.76rem; max-width: 220px; line-height: 1.4; color: rgba(255,255,255,0.85);">
              ${order.address?.street || ""}, ${order.address?.city || ""}, ${order.address?.state || ""} ${order.address?.pincode ? "- " + order.address.pincode : ""}
            </div>
          </td>
          <td>
            ${itemsHtml}
          </td>
          <td>
            <strong style="color: #fff; font-size: 0.95rem;">₹${(Number(order.total) || 0).toLocaleString("en-IN")}</strong>
            <div style="font-size: 0.7rem; color: var(--muted-color); text-transform: uppercase;">Method: ${order.paymentMethod || "COD"}</div>
          </td>
          <td>
            <div style="display: flex; flex-direction: column; gap: 8px; align-items: flex-start;">
              <span class="order-status-badge ${badgeClass}">${order.status}</span>
              <select class="admin-status-select" data-order-id="${order.id}" aria-label="Change Status">
                <option value="Placed">Mark Placed</option>
                <option value="Processing">Mark Processing</option>
                <option value="Shipped">Mark Shipped</option>
                <option value="Delivered">Mark Delivered</option>
                <option value="Cancelled">Cancel Order</option>
              </select>
            </div>
          </td>
        `;

        const selectEl = tr.querySelector(".admin-status-select");
        if (selectEl) {
          selectEl.value = order.status;
          selectEl.addEventListener("change", (e) => {
            updateOrderStatus(order.id, e.target.value);
          });
        }

        tbody.appendChild(tr);
      });
    }

    // Immediate & Robust #admin Hash Detection
    function checkAdminHash() {
      const hash = window.location.hash.toLowerCase();
      if (hash === "#admin" || hash.startsWith("#admin")) {
        // Automatically open Admin Login Modal
        openAdminLoginModal();
      }
    }

    // Run immediately upon script parsing
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", checkAdminHash);
    } else {
      checkAdminHash();
    }

    window.addEventListener("load", checkAdminHash);
    window.addEventListener("hashchange", checkAdminHash);

    // Global helper so user or staff can also type `openAdmin()` directly in browser console
    window.openAdmin = openAdminLoginModal;
    window.admin = openAdminLoginModal;
  </script>
</body>
</html>
"""
