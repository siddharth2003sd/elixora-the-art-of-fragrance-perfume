BODY_HTML = """<body>
  <!-- Custom Luxury Cursor -->
  <div class="custom-cursor" id="custom-cursor"></div>
  <div class="custom-cursor-follower" id="custom-cursor-follower"></div>

  <!-- Dynamic Atmospheric Background & Canvas Particles -->
  <div id="bg-layer"></div>
  <canvas id="particles-canvas"></canvas>

  <!-- Luxury Header -->
  <header class="header" id="main-header">
    <a href="javascript:void(0)" class="brand-logo" id="header-logo" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">
      <div class="logo-symbol" aria-hidden="true"></div>
      <span class="brand-name">ÉLIXORA</span>
    </a>

    <nav class="nav glass" id="desktop-nav" aria-label="Main Navigation">
      <a href="#hero" class="nav-item active">Home</a>
      <a href="#myop-studio" class="nav-item" style="color: var(--gold-light);">✦ Make Your Own</a>
      <a href="#catalog" class="nav-item">Fragrances</a>
      <a href="#discovery" class="nav-item">Discovery Sets</a>
      <a href="#deals" class="nav-item">Deals</a>
      <a href="#stores" class="nav-item">Stores</a>
      <a href="javascript:void(0)" onclick="openCompareModal()" class="nav-item" title="Side-by-side Fragrance Comparison">Compare</a>
      <a href="#story" class="nav-item">About</a>
      <a href="javascript:void(0)" onclick="openTrackOrderModal()" class="nav-item" style="color: var(--gold-light); display: inline-flex; align-items: center; gap: 4px;" title="Track Your Perfume Order">📦 Track Order</a>
    </nav>

    <div class="header-actions">
      <button class="icon-button search-button" id="open-search-btn" aria-label="Search Fragrances">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
      </button>

      <button class="icon-button compare-button" id="open-compare-btn" onclick="openCompareModal()" aria-label="Compare Fragrances" title="Compare Perfumes Side-by-Side">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
          <path d="M16 3h5v5M4 20L21 3M21 16v5h-5M15 15l6 6M4 4l5 5"/>
        </svg>
        <span class="badge-count" id="compare-count-badge">0</span>
      </button>

      <button class="icon-button wishlist-button" id="open-wishlist-btn" aria-label="View Wishlist">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
          <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
        </svg>
        <span class="badge-count" id="wishlist-count-badge">0</span>
      </button>

      <button class="cart-button" id="open-cart-btn" aria-label="Shopping Bag">
        Bag <span id="cart-count-badge">0</span>
      </button>

      <button class="hamburger-btn" id="mobile-menu-btn" aria-label="Open Navigation Menu">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="3" y1="12" x2="21" y2="12"></line>
          <line x1="3" y1="6" x2="21" y2="6"></line>
          <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
      </button>
    </div>
  </header>

  <!-- Mobile Drawer Menu -->
  <div class="drawer-overlay" id="mobile-nav-overlay"></div>
  <div class="drawer-panel" id="mobile-nav-panel" style="right: auto; left: 0; transform: translateX(-100%);">
    <div class="drawer-header">
      <span class="drawer-title">ÉLIXORA</span>
      <button class="close-drawer-btn" id="close-mobile-menu-btn">&times;</button>
    </div>
    <div class="drawer-body" style="padding-top: 2rem; display: flex; flex-direction: column; gap: 4px;">
      <a href="#hero" class="mobile-nav-link" style="color: #fff; font-size: 1.15rem; text-decoration: none; padding: 10px 0;">Home</a>
      <a href="#myop-studio" class="mobile-nav-link" style="color: var(--gold); font-size: 1.15rem; text-decoration: none; padding: 10px 0;">✦ Make Your Own Perfume</a>
      <a href="#catalog" class="mobile-nav-link" style="color: #fff; font-size: 1.15rem; text-decoration: none; padding: 10px 0;">Fragrances Collection</a>
      <a href="#discovery" class="mobile-nav-link" style="color: #fff; font-size: 1.15rem; text-decoration: none; padding: 10px 0;">Discovery Sets (100% Cash-Back)</a>
      <a href="#deals" class="mobile-nav-link" style="color: #fff; font-size: 1.15rem; text-decoration: none; padding: 10px 0;">Scent Deals &amp; Combos</a>
      <a href="#stores" class="mobile-nav-link" style="color: #fff; font-size: 1.15rem; text-decoration: none; padding: 10px 0;">Our 5 Flagship Stores</a>
            <a href="#corporate" class="mobile-nav-link" style="color: #fff; font-size: 1.15rem; text-decoration: none; padding: 10px 0;">Corporate &amp; Wedding Favors</a>
      <a href="javascript:void(0)" onclick="closeMobileMenu(); openCompareModal();" class="mobile-nav-link" style="color: var(--gold-light); font-size: 1.15rem; text-decoration: none; padding: 10px 0;">⚖ Compare Fragrances (<span id="mobile-compare-count">0</span>)</a>
      <a href="javascript:void(0)" onclick="closeMobileMenu(); openTrackOrderModal();" class="mobile-nav-link" style="color: var(--gold-light); font-size: 1.15rem; text-decoration: none; padding: 10px 0; border-top: 1px solid rgba(255,255,255,0.1); margin-top: 10px; padding-top: 14px;">📦 Track Your Order</a>
    </div>
  </div>

  <main>
    <!-- 1. Hero Campaign Section (100% Full-Screen Edge-to-Edge Luxury Advertising Campaign) -->
    <section class="hero-section hero-campaign" id="hero">
      <!-- Ambient Backdrops (Two layers for smooth color blending) -->
      <div id="bg-layer-1" class="bg-layer-base"></div>
      <div id="bg-layer-2" class="bg-layer-transition" style="opacity: 0;"></div>

      <!-- 100% Edge-to-Edge Perfume Photograph Stage (Full Viewport Cover, No Circles, Perfectly Fitted) -->
      <div class="hero-backdrop-stage" id="hero-perfume-carousel-wrap">
        <!-- Full-Screen Hero Image spanning edge to edge without overzooming -->
        <img id="hero-campaign-full-img" class="hero-campaign-full-img" src="/hero_wide_p1.jpg" alt="ÉLIXORA Golden Elixir Eau de Parfum" />
        <img id="hero-campaign-full-img-next" class="hero-campaign-full-img hero-campaign-full-img-next" src="" alt="" aria-hidden="true" />
      </div>

      <!-- Subtle Directional Black-to-Transparent Gradient Behind Text -->
      <div class="hero-campaign-scrim"></div>

      <!-- Subtle Luxury Film Grain Texture -->
      <div class="luxury-grain-overlay"></div>

      <!-- Campaign Product Text Overlay (Placed in the darker / negative space on the left) -->
      <div class="hero-left hero-campaign-content">
        <div class="eyebrow" id="hero-dynamic-brand">ÉLIXORA · LUXURY</div>
        <h1 class="hero-heading" id="hero-dynamic-name">GOLDEN ELIXIR</h1>
        <div class="hero-category-badge-wrap">
          <span class="hero-category-badge" id="hero-dynamic-category">ORIENTAL</span>
          <span class="hero-mood-badge" id="hero-dynamic-mood">warm, luxurious, sensual</span>
        </div>
        <p class="hero-tagline" id="hero-dynamic-desc">
          An opulent stream of golden amber, warm cashmeran woods, and honeyed saffron threads, radiating an irresistible, seductive warmth.
        </p>
        <div class="hero-actions">
          <button class="primary-btn" id="hero-discover-btn">
            DISCOVER FRAGRANCE
            <span>+</span>
          </button>
        </div>
      </div>

      <!-- Left Side Corner Arrow Navigation -->
      <button class="hero-edge-nav-btn hero-edge-prev" id="hero-carousel-prev-btn" aria-label="Previous Fragrance" title="Previous Fragrance">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
      </button>

      <!-- Right Side Corner Arrow Navigation -->
      <button class="hero-edge-nav-btn hero-edge-next" id="hero-carousel-next-btn" aria-label="Next Fragrance" title="Next Fragrance">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="9 18 15 12 9 6"></polyline>
        </svg>
      </button>



      <!-- Hidden container to retain data-theme pill elements for existing JS selectors -->
      <div class="theme-morph-bar" style="display: none !important;" aria-hidden="true">
        <span class="theme-morph-label">Fragrance Aura:</span>
        <div class="theme-pills">
          <button class="theme-pill-btn active" data-theme="p1">Amber Gold</button>
          <button class="theme-pill-btn" data-theme="p2">Ocean Blue</button>
          <button class="theme-pill-btn" data-theme="p3">Rose Pink</button>
          <button class="theme-pill-btn" data-theme="p4">Midnight Black</button>
          <button class="theme-pill-btn" data-theme="p5">Emerald Green</button>
          <button class="theme-pill-btn" data-theme="p6">Royal Purple</button>
          <button class="theme-pill-btn" data-theme="p7">Crystal Clear</button>
          <button class="theme-pill-btn" data-theme="p8">Ruby Red</button>
          <button class="theme-pill-btn" data-theme="p9">Turquoise</button>
          <button class="theme-pill-btn" data-theme="p10">Peach Nude</button>
          <button class="theme-pill-btn" data-theme="p11">Forest Green</button>
          <button class="theme-pill-btn" data-theme="p12">Lavender</button>
          <button class="theme-pill-btn" data-theme="p13">Golden Sand</button>
          <button class="theme-pill-btn" data-theme="p14">Sapphire Blue</button>
          <button class="theme-pill-btn" data-theme="p15">Ivory White</button>
          <button class="theme-pill-btn" data-theme="p16">Silver</button>
          <button class="theme-pill-btn" data-theme="p17">Coral</button>
          <button class="theme-pill-btn" data-theme="p18">Amethyst Pink</button>
          <button class="theme-pill-btn" data-theme="p19">Sea Foam</button>
          <button class="theme-pill-btn" data-theme="p20">Espresso Brown</button>
        </div>
      </div>
    </section>

    <!-- ==========================================================
         MYOP: MAKE YOUR OWN PERFUME BLENDING STUDIO
         ========================================================== -->
    <section class="myop-studio-section" id="myop-studio">
      <div class="myop-hero-banner">
        <div class="myop-banner-content">
          <span class="section-eyebrow">INDIA'S FIRST PERFUME BAR CONCEPT</span>
          <h3>Make Your Own Perfume</h3>
          <p>
            Why wear someone else's formula when you can author your own? Blend hand-selected European botanical oils with India's highest 50% oil concentration for an extraordinary 18–24 hour projection in tropical climates.
          </p>
          <div class="tropical-badge-large">
            <span>&#9889; 50% High Oil Concentration</span> &middot; <span>24H Tropical Heat Endurance</span> &middot; <span>Free Laser Engraving</span>
          </div>
        </div>
      </div>

      <div class="myop-studio-grid">
        <!-- Studio Left: Stepper & Controls -->
        <div class="studio-panel">
          <!-- Stepper Navigation Tabs -->
          <div class="studio-stepper-nav" id="studio-stepper-nav">
            <button class="studio-step-tab active" onclick="switchStudioStep(1)">1. Flacon &amp; Size</button>
            <button class="studio-step-tab" onclick="switchStudioStep(2)">2. Base Oil (50%)</button>
            <button class="studio-step-tab" onclick="switchStudioStep(3)">3. Heart &amp; Accents</button>
            <button class="studio-step-tab" onclick="switchStudioStep(4)">4. Blending Ratio</button>
            <button class="studio-step-tab" onclick="switchStudioStep(5)">5. Name &amp; Engrave</button>
          </div>

          <!-- Step 1: Flacon & Size -->
          <div class="studio-step-content" id="studio-step-pane-1">
            <div style="margin-bottom: 1rem;">
              <span class="custom-field-label">Select Flacon Architecture &amp; Volume:</span>
            </div>
            <div class="flacon-picker-grid">
              <div class="flacon-choice-card" onclick="selectStudioFlacon('50ml', 1499, this)">
                <svg class="flacon-icon-svg" viewBox="0 0 24 34" fill="none" stroke="currentColor" stroke-width="1.8">
                  <rect x="7" y="2" width="10" height="6" rx="1"></rect>
                  <path d="M5 8h14v22a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V8z"></path>
                </svg>
                <div class="flacon-size-title">50ml</div>
                <div class="flacon-size-desc">Pocket &middot; Travel Ready</div>
                <div class="flacon-size-price">₹1,499</div>
              </div>

              <div class="flacon-choice-card selected" onclick="selectStudioFlacon('100ml', 2499, this)">
                <span class="flacon-popular-badge">MOST POPULAR</span>
                <svg class="flacon-icon-svg" viewBox="0 0 24 34" fill="none" stroke="currentColor" stroke-width="1.8">
                  <rect x="6" y="2" width="12" height="6" rx="1"></rect>
                  <path d="M4 8h16v23a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V8z"></path>
                </svg>
                <div class="flacon-size-title">100ml</div>
                <div class="flacon-size-desc">Signature &middot; Master Decanter</div>
                <div class="flacon-size-price">₹2,499</div>
              </div>

              <div class="flacon-choice-card" onclick="selectStudioFlacon('120ml', 3199, this)">
                <svg class="flacon-icon-svg" viewBox="0 0 24 34" fill="none" stroke="currentColor" stroke-width="1.8">
                  <rect x="5" y="2" width="14" height="6" rx="1"></rect>
                  <path d="M3 8h18v24a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8z"></path>
                </svg>
                <div class="flacon-size-title">120ml</div>
                <div class="flacon-size-desc">Grand Decanter &middot; Collector</div>
                <div class="flacon-size-price">₹3,199</div>
              </div>
            </div>

            <!-- Flacon Finish -->
            <span class="custom-field-label">Flacon Cap &amp; Collar Finish:</span>
            <div class="finish-selector-row">
              <button class="finish-pill-btn selected" onclick="selectStudioFinish('Obsidian Noir', '#1a1a1a', this)">
                <span class="finish-dot" style="background: #111;"></span> Obsidian Noir
              </button>
              <button class="finish-pill-btn" onclick="selectStudioFinish('Champagne Gold', '#d4af70', this)">
                <span class="finish-dot" style="background: #d4af70;"></span> 24K Champagne Gold
              </button>
              <button class="finish-pill-btn" onclick="selectStudioFinish('Platinum Silver', '#e2e8f0', this)">
                <span class="finish-dot" style="background: #e2e8f0;"></span> Platinum Silver
              </button>
            </div>

            <button class="secondary-btn" style="margin-top: 2rem; width: 100%;" onclick="switchStudioStep(2)">
              Next: Select Base Oil (50%) &rarr;
            </button>
          </div>

          <!-- Step 2: Base Oil Selection -->
          <div class="studio-step-content" id="studio-step-pane-2" style="display: none;">
            <div style="margin-bottom: 1rem;">
              <span class="custom-field-label">Select 1 European Base Perfume Oil (Concentration: 50%):</span>
            </div>
            <div class="oils-selector-grid">
              <div class="oil-card selected" onclick="selectBaseOil('Mysore Sandalwood', 'India', 'Creamy woody serenity with enduring warmth', '#d4af70', this)">
                <span class="oil-origin-label">Mysore &middot; India</span>
                <h4 class="oil-card-title">Mysore Sandalwood</h4>
                <p class="oil-card-desc">Warm, velvety timber distilled from 40-year aged sacred wood.</p>
                <span class="oil-tag-pill">Woody &middot; Serene</span>
              </div>

              <div class="oil-card" onclick="selectBaseOil('Royal Assam Oud', 'Assam, India', 'Smoky agarwood resin with animalic magnetic mystery', '#78350f', this)">
                <span class="oil-origin-label">Assam &middot; India</span>
                <h4 class="oil-card-title">Royal Assam Oud</h4>
                <p class="oil-card-desc">Dark agarwood aged in underground copper vats. Regal &amp; smoky.</p>
                <span class="oil-tag-pill">Resinous &middot; Smoky</span>
              </div>

              <div class="oil-card" onclick="selectBaseOil('Toasted Tonka', 'Venezuela', 'Sweet almond and balsamic spice with toasted caramel notes', '#b45309', this)">
                <span class="oil-origin-label">Venezuela</span>
                <h4 class="oil-card-title">Toasted Tonka</h4>
                <p class="oil-card-desc">Dark, aromatic tonka beans roasted and infused with spiced balsamic sweetness.</p>
                <span class="oil-tag-pill">Gourmand &middot; Warm</span>
              </div>

              <div class="oil-card" onclick="selectBaseOil('Golden Fossil Amber', 'Baltic', 'Molten honeycomb and balsamic pine resin warmth', '#ca8a04', this)">
                <span class="oil-origin-label">Baltic Coast</span>
                <h4 class="oil-card-title">Fossil Amber</h4>
                <p class="oil-card-desc">Ancient coniferous sap fossilized into sweet resinous gold.</p>
                <span class="oil-tag-pill">Amber &middot; Balsamic</span>
              </div>

              <div class="oil-card" onclick="selectBaseOil('Haitian Vetiver', 'Haiti', 'Smoked earthy root with aristocratic grassy richness', '#166534', this)">
                <span class="oil-origin-label">Les Cayes &middot; Haiti</span>
                <h4 class="oil-card-title">Smoked Vetiver</h4>
                <p class="oil-card-desc">Cold-washed roots offering refined earthy dampness and smoky flair.</p>
                <span class="oil-tag-pill">Earthy &middot; Crisp</span>
              </div>

              <div class="oil-card" onclick="selectBaseOil('Atlas Cedarwood', 'Morocco', 'Dry cedar bough with comforting resinous cedar bark', '#92400e', this)">
                <span class="oil-origin-label">Atlas Mountains</span>
                <h4 class="oil-card-title">Atlas Cedarwood</h4>
                <p class="oil-card-desc">High-altitude coniferous wood with clean, dignified timber facets.</p>
                <span class="oil-tag-pill">Dry Timber</span>
              </div>

              <div class="oil-card" onclick="selectBaseOil('White Cashmere Musk', 'Grasse, France', 'Sensual silk skin warmth with radiant clean magnetism', '#94a3b8', this)">
                <span class="oil-origin-label">Grasse &middot; France</span>
                <h4 class="oil-card-title">Cashmere Musk</h4>
                <p class="oil-card-desc">Botanical clean musk replicating intimate skin contact.</p>
                <span class="oil-tag-pill">Intimate Skin</span>
              </div>
            </div>

            <div style="display: flex; gap: 1rem; margin-top: 1.5rem;">
              <button class="secondary-btn" style="flex: 1;" onclick="switchStudioStep(1)">&larr; Back</button>
              <button class="secondary-btn" style="flex: 1;" onclick="switchStudioStep(3)">Next: Heart Notes &rarr;</button>
            </div>
          </div>

          <!-- Step 3: Heart & Accent Notes -->
          <div class="studio-step-content" id="studio-step-pane-3" style="display: none;">
            <div style="margin-bottom: 1rem;">
              <span class="custom-field-label">Select 1 or 2 Heart &amp; Accent Notes:</span>
            </div>
            <div class="heart-notes-grid">
              <div class="heart-note-pill selected" onclick="toggleHeartNote('Grasse Rose Centifolia', this)">
                <span class="heart-note-icon">&#10047;</span>
                <span class="heart-note-name">Grasse Rose</span>
                <span class="heart-note-family">Floral May Dawn</span>
              </div>
              <div class="heart-note-pill" onclick="toggleHeartNote('Madurai Jasmine Sambac', this)">
                <span class="heart-note-icon">&#10048;</span>
                <span class="heart-note-name">Jasmine Sambac</span>
                <span class="heart-note-family">Nocturnal White Bloom</span>
              </div>
              <div class="heart-note-pill" onclick="toggleHeartNote('Calabrian Bergamot', this)">
                <span class="heart-note-icon">&#10034;</span>
                <span class="heart-note-name">Calabrian Bergamot</span>
                <span class="heart-note-family">Sun-Drenched Citrus</span>
              </div>
              <div class="heart-note-pill" onclick="toggleHeartNote('Atlantic Sea Salt', this)">
                <span class="heart-note-icon">&#10038;</span>
                <span class="heart-note-name">Sea Salt Drift</span>
                <span class="heart-note-family">Marine Saline Breeze</span>
              </div>
              <div class="heart-note-pill" onclick="toggleHeartNote('Dark Cacao &amp; Tonka', this)">
                <span class="heart-note-icon">&#9830;</span>
                <span class="heart-note-name">Dark Cacao</span>
                <span class="heart-note-family">Bitter Almond &amp; Tonka</span>
              </div>
              <div class="heart-note-pill" onclick="toggleHeartNote('Cardamom &amp; Saffron', this)">
                <span class="heart-note-icon">&#10022;</span>
                <span class="heart-note-name">Saffron Spice</span>
                <span class="heart-note-family">Warm Cardamom Pods</span>
              </div>
              <div class="heart-note-pill" onclick="toggleHeartNote('French Lavender', this)">
                <span class="heart-note-icon">&#10049;</span>
                <span class="heart-note-name">Alpine Lavender</span>
                <span class="heart-note-family">Aromatic Herb Calm</span>
              </div>
              <div class="heart-note-pill" onclick="toggleHeartNote('Sicilian Neroli', this)">
                <span class="heart-note-icon">&#10047;</span>
                <span class="heart-note-name">Orange Blossom</span>
                <span class="heart-note-family">Honeyed Neroli Petals</span>
              </div>
            </div>

            <div style="display: flex; gap: 1rem; margin-top: 1.5rem;">
              <button class="secondary-btn" style="flex: 1;" onclick="switchStudioStep(2)">&larr; Back</button>
              <button class="secondary-btn" style="flex: 1;" onclick="switchStudioStep(4)">Next: Blending Ratio &rarr;</button>
            </div>
          </div>

          <!-- Step 4: Proportion & Oil Guarantee -->
          <div class="studio-step-content" id="studio-step-pane-4" style="display: none;">
            <span class="custom-field-label">Custom Blending Ratio (% Base vs % Heart):</span>
            <div class="ratio-slider-box">
              <div class="ratio-labels-row">
                <span>Base Oil Proportion: <strong id="ratio-base-val" style="color: var(--gold);">60%</strong></span>
                <span>Heart Notes Proportion: <strong id="ratio-heart-val" style="color: var(--cream);">40%</strong></span>
              </div>
              <input type="range" class="ratio-slider-input" id="studio-ratio-slider" min="30" max="80" value="60" oninput="handleStudioRatio(this.value)" />

              <div class="ratio-breakdown-metrics">
                <div>
                  <div class="metric-item-val" id="metric-oil-pct">50%</div>
                  <div class="metric-item-lbl">Pure Perfume Oil</div>
                </div>
                <div>
                  <div class="metric-item-val" id="metric-longevity">24 Hours</div>
                  <div class="metric-item-lbl">Tropical Longevity</div>
                </div>
                <div>
                  <div class="metric-item-val" id="metric-sillage">Heavy / 2m</div>
                  <div class="metric-item-lbl">Sillage Radius</div>
                </div>
              </div>
            </div>

            <div class="oil-guarantee-card">
              <div class="oil-guarantee-icon">&#128737;</div>
              <div class="oil-guarantee-info">
                <h4>MYOP 50% Tropical Longevity Formulation</h4>
                <p>
                  Standard retail perfumes dilute down to 10–15% oil, evaporating within hours in warm weather. ÉLIXORA / MYOP blends contain an unprecedented 50% concentration of pure European oils that bond tightly to human skin lipids.
                </p>
              </div>
            </div>

            <div style="display: flex; gap: 1rem; margin-top: 1.5rem;">
              <button class="secondary-btn" style="flex: 1;" onclick="switchStudioStep(3)">&larr; Back</button>
              <button class="secondary-btn" style="flex: 1;" onclick="switchStudioStep(5)">Next: Name Perfume &rarr;</button>
            </div>
          </div>

          <!-- Step 5: Name Your Creation -->
          <div class="studio-step-content" id="studio-step-pane-5" style="display: none;">
            <div class="custom-name-field-wrap">
              <label class="custom-field-label" for="custom-blend-name-input">Give Your Creation a Name:</label>
              <input type="text" class="custom-text-input" id="custom-blend-name-input" placeholder="e.g. Sovereign Oud, Velvet Midnight, Aura No. 7" maxlength="28" value="Aura Sovereign" oninput="updateCustomBottleName(this.value)" />
            </div>

            <div style="display: flex; gap: 1rem; margin-top: 1.5rem;">
              <button class="secondary-btn" style="flex: 1;" onclick="switchStudioStep(4)">&larr; Back</button>
              <button class="primary-btn" style="flex: 1.5;" onclick="addCustomBlendToBag()">
                ✦ Add Bespoke Blend to Bag
              </button>
            </div>
          </div>
        </div>

        <!-- Studio Right: Sticky Flacon Live Visualizer -->
        <div class="flacon-visualizer-sticky">
          <span class="batch-id-chip" id="custom-formula-batch-code">#MYOP-8492-GRASSE</span>
          <h3 style="font-family: var(--heading-font); font-size: 1.6rem; color: #fff; margin: 0.6rem 0 0.3rem 0;" id="visualizer-blend-name">
            Aura Sovereign
          </h3>
          <p style="font-size: 0.75rem; color: var(--gold); letter-spacing: 0.08em; text-transform: uppercase;" id="visualizer-flacon-tag">
            100ml Extrait de Parfum &middot; 50% Oil
          </p>

          <!-- Bottle Graphic Stage with Dynamic Tint -->
          <div class="flacon-visualizer-glass">
            <img class="flacon-rendered-bottle" id="studio-flacon-img" src="/elixora_hero_bottle.jpg" alt="Bespoke Perfume Flacon" />
            <div class="flacon-tint-layer" id="studio-tint-layer"></div>
            <div class="flacon-engraving-rendered" id="studio-live-engraving" style="display: none;">
              SIDDHARTH
            </div>
          </div>

          <!-- Formula Summary Card -->
          <div class="formula-breakdown-card">
            <div class="formula-row">
              <span>Flacon Size:</span>
              <strong id="card-size-label">100ml Decanter</strong>
            </div>
            <div class="formula-row">
              <span>Base Essence (50%):</span>
              <strong id="card-base-label">Mysore Sandalwood</strong>
            </div>
            <div class="formula-row">
              <span>Heart &amp; Accents:</span>
              <strong id="card-heart-label">Grasse Rose Centifolia</strong>
            </div>
            <div class="formula-row">
              <span>Ratio:</span>
              <strong id="card-ratio-label">60% Base / 40% Heart</strong>
            </div>
          </div>

          <div class="custom-blend-price-row">
            <div>
              <span style="font-size: 0.72rem; color: var(--muted-color); display: block;">Total All-Inclusive:</span>
              <span class="custom-blend-price" id="studio-price-val">₹2,499</span>
            </div>
            <span class="custom-blend-oil-tag">✓ 50% Tropical Oil</span>
          </div>

          <button class="primary-btn" style="width: 100%;" onclick="addCustomBlendToBag()">
            ✦ ADD BESPOKE BLEND TO BAG &rarr;
          </button>
        </div>
      </div>
    </section>

    <!-- 2. Fragrance Collections (Explore By Fragrance) -->
    <section class="section-container" id="collections">
      <div class="section-header">
        <span class="section-eyebrow">THE OLFACTORY FAMILIES</span>
        <h2 class="section-title">Explore by Fragrance</h2>
        <p class="section-subtitle">
          Find the mood that speaks directly to your spirit. Each olfactory family embodies a distinct universe of emotion.
        </p>
      </div>

      <div class="collections-grid">
        <!-- Floral -->
        <div class="collection-card" onclick="filterCatalogBy('FLORAL')">
          <img class="collection-bg-img" src="/elixora_rose_bottle.jpg" alt="Floral Fragrances" />
          <div class="collection-overlay"></div>
          <div class="collection-content">
            <span class="collection-family">COLLECTION 01</span>
            <h3 class="collection-name">FLORAL</h3>
            <p class="collection-desc">Ethereal May roses, velvety jasmine sambac and delicate orris butter distilled in the dawn light of Grasse.</p>
            <div class="collection-notes-list">
              <span class="collection-note-pill">Rose Damascena</span>
              <span class="collection-note-pill">Jasmine Sambac</span>
              <span class="collection-note-pill">Peony</span>
              <span class="collection-note-pill">Iris Pallida</span>
            </div>
            <div class="collection-extra-details">
              <div class="collection-meta-row">
                <span class="collection-meta-item"><em>Origin:</em> Grasse &amp; Isparta</span>
                <span class="collection-meta-item"><em>Intensity:</em> Moderate &middot; Radiant</span>
              </div>
              <span class="collection-explore-btn">Explore Collection &rarr;</span>
            </div>
          </div>
        </div>

        <!-- Woody -->
        <div class="collection-card" onclick="filterCatalogBy('WOODY')">
          <img class="collection-bg-img" src="/elixora_oud_bottle.jpg" alt="Woody Fragrances" />
          <div class="collection-overlay"></div>
          <div class="collection-content">
            <span class="collection-family">COLLECTION 02</span>
            <h3 class="collection-name">WOODY</h3>
            <p class="collection-desc">Sacred aged agarwood, creamy Mysore sandalwood, and smoked vetiver steeped in deep forest mystery.</p>
            <div class="collection-notes-list">
              <span class="collection-note-pill">Mysore Sandalwood</span>
              <span class="collection-note-pill">Atlas Cedar</span>
              <span class="collection-note-pill">Haitian Vetiver</span>
              <span class="collection-note-pill">Smoked Oud</span>
            </div>
            <div class="collection-extra-details">
              <div class="collection-meta-row">
                <span class="collection-meta-item"><em>Origin:</em> Cambodia &amp; Mysore</span>
                <span class="collection-meta-item"><em>Intensity:</em> Deep &middot; Resinous</span>
              </div>
              <span class="collection-explore-btn">Explore Collection &rarr;</span>
            </div>
          </div>
        </div>

        <!-- Fresh -->
        <div class="collection-card" onclick="filterCatalogBy('FRESH')">
          <img class="collection-bg-img" src="/elixora_aqua_bottle.jpg" alt="Fresh Fragrances" />
          <div class="collection-overlay"></div>
          <div class="collection-content">
            <span class="collection-family">COLLECTION 03</span>
            <h3 class="collection-name">FRESH</h3>
            <p class="collection-desc">Crisp sea salt breezes, sun-ripened Calabrian citrus groves, and crystalline spring dew drops.</p>
            <div class="collection-notes-list">
              <span class="collection-note-pill">Calabrian Bergamot</span>
              <span class="collection-note-pill">Marine Accord</span>
              <span class="collection-note-pill">Crushed Mint</span>
              <span class="collection-note-pill">White Tea</span>
            </div>
            <div class="collection-extra-details">
              <div class="collection-meta-row">
                <span class="collection-meta-item"><em>Origin:</em> Amalfi &amp; Capri</span>
                <span class="collection-meta-item"><em>Intensity:</em> Luminous &middot; Crisp</span>
              </div>
              <span class="collection-explore-btn">Explore Collection &rarr;</span>
            </div>
          </div>
        </div>

        <!-- Oriental -->
        <div class="collection-card" onclick="filterCatalogBy('ORIENTAL')">
          <img class="collection-bg-img" src="/elixora_hero_bottle.jpg" alt="Oriental Fragrances" />
          <div class="collection-overlay"></div>
          <div class="collection-content">
            <span class="collection-family">COLLECTION 04</span>
            <h3 class="collection-name">ORIENTAL</h3>
            <p class="collection-desc">Nocturnal amber, molten benzoin, roasted spices, and dark opulent silks woven for royalty.</p>
            <div class="collection-notes-list">
              <span class="collection-note-pill">Golden Amber</span>
              <span class="collection-note-pill">Toasted Tonka</span>
              <span class="collection-note-pill">Cardamom</span>
              <span class="collection-note-pill">Musk Velvet</span>
            </div>
            <div class="collection-extra-details">
              <div class="collection-meta-row">
                <span class="collection-meta-item"><em>Origin:</em> Oman &amp; Persia</span>
                <span class="collection-meta-item"><em>Intensity:</em> Intoxicating &middot; Long-lasting</span>
              </div>
              <span class="collection-explore-btn">Explore Collection &rarr;</span>
            </div>
          </div>
        </div>

        <!-- Gourmand -->
        <div class="collection-card" onclick="filterCatalogBy('GOURMAND')">
          <img class="collection-bg-img" src="/elixora_oud_bottle.jpg" alt="Gourmand Fragrances" />
          <div class="collection-overlay"></div>
          <div class="collection-content">
            <span class="collection-family">COLLECTION 05</span>
            <h3 class="collection-name">GOURMAND</h3>
            <p class="collection-desc">Sweetened hazelnut paste, bittersweet Venezuelan cocoa nibs, and toasted praline confection.</p>
            <div class="collection-notes-list">
              <span class="collection-note-pill">Salted Caramel</span>
              <span class="collection-note-pill">Dark Cacao</span>
              <span class="collection-note-pill">Roasted Tonka</span>
              <span class="collection-note-pill">Praline</span>
            </div>
            <div class="collection-extra-details">
              <div class="collection-meta-row">
                <span class="collection-meta-item"><em>Origin:</em> Madagascar &amp; Arriba</span>
                <span class="collection-meta-item"><em>Intensity:</em> Warm &middot; Addictive</span>
              </div>
              <span class="collection-explore-btn">Explore Collection &rarr;</span>
            </div>
          </div>
        </div>

        <!-- Citrus -->
        <div class="collection-card" onclick="filterCatalogBy('CITRUS')">
          <img class="collection-bg-img" src="/elixora_aqua_bottle.jpg" alt="Citrus Fragrances" />
          <div class="collection-overlay"></div>
          <div class="collection-content">
            <span class="collection-family">COLLECTION 06</span>
            <h3 class="collection-name">CITRUS</h3>
            <p class="collection-desc">Radiant Sicilian oranges, sunlit Sorrento lemon blossoms, and sparkling herbaceous neroli.</p>
            <div class="collection-notes-list">
              <span class="collection-note-pill">Blood Orange</span>
              <span class="collection-note-pill">Amalfi Lemon</span>
              <span class="collection-note-pill">Ruby Grapefruit</span>
              <span class="collection-note-pill">Neroli Blossom</span>
            </div>
            <div class="collection-extra-details">
              <div class="collection-meta-row">
                <span class="collection-meta-item"><em>Origin:</em> Sicily &amp; Calabria</span>
                <span class="collection-meta-item"><em>Intensity:</em> Effervescent &middot; Uplifting</span>
              </div>
              <span class="collection-explore-btn">Explore Collection &rarr;</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. The Collection / Product Catalog -->
    <section class="section-container" id="catalog">
      <div class="section-header centered">
        <span class="section-eyebrow">HAUTE PARFUMERIE</span>
        <h2 class="section-title">The Collection</h2>
        <p class="section-subtitle">
          Curated masterworks distilled by world-renowned noses. Filter by mood, gender, and concentration.
        </p>
      </div>

      <div class="catalog-controls">
        <div class="catalog-filter-row">
          <div class="filter-pills" id="catalog-filter-pills">
            <button class="filter-btn active" data-filter="ALL">ALL</button>
            <button class="filter-btn" data-filter="MEN">MEN</button>
            <button class="filter-btn" data-filter="WOMEN">WOMEN</button>
            <button class="filter-btn" data-filter="UNISEX">UNISEX</button>
            <button class="filter-btn" data-filter="FLORAL">FLORAL</button>
            <button class="filter-btn" data-filter="WOODY">WOODY</button>
            <button class="filter-btn" data-filter="FRESH">FRESH</button>
            <button class="filter-btn" data-filter="ORIENTAL">ORIENTAL</button>
            <button class="filter-btn" data-filter="GOURMAND">GOURMAND</button>
          </div>

          <div class="catalog-sort-group">
            <label for="catalog-sort-select" class="sort-label">Sort by:</label>
            <select id="catalog-sort-select" class="custom-select">
              <option value="featured">Featured</option>
              <option value="price-asc">Price: Low &rarr; High</option>
              <option value="price-desc">Price: High &rarr; Low</option>
              <option value="rating">Best Rated</option>
              <option value="newest">Newest</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Catalog Compare Interactive Prompt Banner -->
      <div class="catalog-compare-banner">
        <div class="compare-banner-left">
          <span class="compare-icon-badge">⚖</span>
          <div>
            <strong>Interactive Perfume Comparison Studio:</strong>
            <span>Select <em>Compare</em> on any two perfumes below to evaluate olfactory notes, 50% tropical oil concentration, and price side-by-side.</span>
          </div>
        </div>
        <button class="compare-banner-btn" onclick="openCompareModal()">
          Launch Compare Studio ⚖
        </button>
      </div>

      <!-- Product Cards Carousel System -->
      <div class="products-carousel-wrapper" id="products-carousel-wrapper">
        <button class="carousel-arrow-btn prev-btn" id="carousel-prev-btn" aria-label="Previous Fragrance" title="Previous Fragrance">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="15 18 9 12 15 6"></polyline>
          </svg>
        </button>

        <div class="carousel-viewport" id="carousel-viewport">
          <div class="products-grid" id="products-grid">
            <!-- Rendered dynamically via JavaScript -->
          </div>
        </div>

        <button class="carousel-arrow-btn next-btn" id="carousel-next-btn" aria-label="Next Fragrance" title="Next Fragrance">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="9 18 15 12 9 6"></polyline>
          </svg>
        </button>

        <div class="carousel-footer-bar">
          <div class="carousel-autoplay-status" id="carousel-autoplay-status">
            <span class="autoplay-pulse-dot"></span>
            <span id="carousel-status-text">Auto-Advancing every 3s</span>
          </div>
          <div class="carousel-dots-wrap" id="carousel-dots-wrap">
            <!-- Dots dynamically populated -->
          </div>
        </div>
      </div>
    </section>

    <!-- ==========================================================
         DISCOVERY SETS & SAMPLE VAULTS (100% CASH-BACK)
         ========================================================== -->
    <section class="discovery-section" id="discovery">
      <div class="section-header centered">
        <span class="section-eyebrow">RISK-FREE OLFACTORY EXPLORATION</span>
        <h2 class="section-title">The Discovery Sets</h2>
        <p class="section-subtitle">
          Sample 5 exquisite signature fragrances before committing to a full 100ml decanter. Every discovery set includes a <strong>100% Cash-Back Coupon (₹999)</strong> redeemable against your next full-size bottle.
        </p>
      </div>

      <div class="discovery-grid">
        <!-- Set 1 -->
        <div class="discovery-card">
          <div class="discovery-img-wrap">
            <img class="discovery-img" src="/golden_elixir.jpg" alt="The ÉLIXORA Flagship Golden Elixir Flacon" />
            <span class="cashback-badge">&#10022; 100% CASH-BACK VOUCHER</span>
          </div>
          <div class="discovery-body">
            <span class="discovery-badge">5 &times; 5ml Extrait Sprays</span>
            <h3 class="discovery-title">The ÉLIXORA Flagship Icons Vault</h3>
            <p class="discovery-desc">
              Experience ÉLIXORA's 5 most celebrated award-winning creations: Golden Elixir, Azure Mist, Rose Éclat, Noir Intense, and Rouge Passion.
            </p>
            <div class="vials-row">
              <span class="vial-pill" onclick="openProductModal('p1')" style="cursor: pointer;" title="Explore Golden Elixir">5ml Golden Elixir</span>
              <span class="vial-pill" onclick="openProductModal('p2')" style="cursor: pointer;" title="Explore Azure Mist">5ml Azure Mist</span>
              <span class="vial-pill" onclick="openProductModal('p3')" style="cursor: pointer;" title="Explore Rose Éclat">5ml Rose Éclat</span>
              <span class="vial-pill" onclick="openProductModal('p4')" style="cursor: pointer;" title="Explore Noir Intense">5ml Noir Intense</span>
              <span class="vial-pill" onclick="openProductModal('p8')" style="cursor: pointer;" title="Explore Rouge Passion">5ml Rouge Passion</span>
            </div>
            <div class="discovery-price-row">
              <div>
                <span class="discovery-price">₹999</span>
                <span class="discovery-orig-price">₹1,999</span>
              </div>
              <button class="primary-btn" onclick="addDiscoverySetToBag('The ÉLIXORA Flagship Icons Vault', 999, '/golden_elixir.jpg')">
                + Add to Bag
              </button>
            </div>
          </div>
        </div>

        <!-- Set 2 -->
        <div class="discovery-card">
          <div class="discovery-img-wrap">
            <img class="discovery-img" src="/emerald_woods.jpg" alt="ÉLIXORA Woods &amp; Royal Orientals Emerald Flacon" />
            <span class="cashback-badge">&#10022; 100% CASH-BACK VOUCHER</span>
          </div>
          <div class="discovery-body">
            <span class="discovery-badge">5 &times; 5ml Extrait Sprays</span>
            <h3 class="discovery-title">ÉLIXORA Woods &amp; Royal Orientals Vault</h3>
            <p class="discovery-desc">
              For connoisseurs of profound depth and smoky resins: Emerald Woods, Green Oud, Desert Gold, Sapphire Noir, and Café Noir.
            </p>
            <div class="vials-row">
              <span class="vial-pill" onclick="openProductModal('p5')" style="cursor: pointer;" title="Explore Emerald Woods">5ml Emerald Woods</span>
              <span class="vial-pill" onclick="openProductModal('p11')" style="cursor: pointer;" title="Explore Green Oud">5ml Green Oud</span>
              <span class="vial-pill" onclick="openProductModal('p13')" style="cursor: pointer;" title="Explore Desert Gold">5ml Desert Gold</span>
              <span class="vial-pill" onclick="openProductModal('p14')" style="cursor: pointer;" title="Explore Sapphire Noir">5ml Sapphire Noir</span>
              <span class="vial-pill" onclick="openProductModal('p20')" style="cursor: pointer;" title="Explore Café Noir">5ml Café Noir</span>
            </div>
            <div class="discovery-price-row">
              <div>
                <span class="discovery-price">₹1,199</span>
                <span class="discovery-orig-price">₹2,299</span>
              </div>
              <button class="primary-btn" onclick="addDiscoverySetToBag('ÉLIXORA Woods &amp; Royal Orientals Vault', 1199, '/emerald_woods.jpg')">
                + Add to Bag
              </button>
            </div>
          </div>
        </div>

        <!-- Set 3 -->
        <div class="discovery-card">
          <div class="discovery-img-wrap">
            <img class="discovery-img" src="/aqua_lumiere.jpg" alt="ÉLIXORA Luminous Florals &amp; Marine Aqua Flacon" />
            <span class="cashback-badge">&#10022; 100% CASH-BACK VOUCHER</span>
          </div>
          <div class="discovery-body">
            <span class="discovery-badge">5 &times; 5ml Pure Sprays</span>
            <h3 class="discovery-title">ÉLIXORA Luminous Florals &amp; Marine Vault</h3>
            <p class="discovery-desc">
              Radiant sunlit botanicals and sparkling ocean tides: Aqua Lumière, Royal Amethyst, Pure Crystal, Coral Bliss, and Ocean Veil.
            </p>
            <div class="vials-row">
              <span class="vial-pill" onclick="openProductModal('p9')" style="cursor: pointer;" title="Explore Aqua Lumière">5ml Aqua Lumière</span>
              <span class="vial-pill" onclick="openProductModal('p6')" style="cursor: pointer;" title="Explore Royal Amethyst">5ml Royal Amethyst</span>
              <span class="vial-pill" onclick="openProductModal('p7')" style="cursor: pointer;" title="Explore Pure Crystal">5ml Pure Crystal</span>
              <span class="vial-pill" onclick="openProductModal('p17')" style="cursor: pointer;" title="Explore Coral Bliss">5ml Coral Bliss</span>
              <span class="vial-pill" onclick="openProductModal('p19')" style="cursor: pointer;" title="Explore Ocean Veil">5ml Ocean Veil</span>
            </div>
            <div class="discovery-price-row">
              <div>
                <span class="discovery-price">₹899</span>
                <span class="discovery-orig-price">₹1,799</span>
              </div>
              <button class="primary-btn" onclick="addDiscoverySetToBag('ÉLIXORA Luminous Florals &amp; Marine Vault', 899, '/aqua_lumiere.jpg')">
                + Add to Bag
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==========================================================
         SCENT DEALS & EXCLUSIVE COMBOS
         ========================================================== -->
    <section class="deals-section" id="deals">
      <div class="section-header centered">
        <span class="section-eyebrow">CURATED CONNOISSEUR OFFERS</span>
        <h2 class="section-title">Scent Deals &amp; Bundles</h2>
        <p class="section-subtitle">
          Elevate your olfactory wardrobe with exclusive multi-bottle value collections and celebratory gifting sets.
        </p>
      </div>

      <div class="deals-grid">
        <!-- Deal 1 -->
        <div class="deal-card featured">
          <div class="deal-badge-pill">LIMITED TIME PROMO</div>
          <h3 class="deal-title">BUY 2 GET 1 FREE</h3>
          <p class="deal-desc">
            Purchase any two 100ml flacons across the entire ÉLIXORA or MYOP collection, and receive a 3rd 100ml fragrance completely complimentary.
          </p>
          <div class="deal-features">
            <div class="deal-feature-item">
              <span style="color: var(--gold);">&#10003;</span>
              <span>Valid across all 50% Tropical Oil concentrations</span>
            </div>
            <div class="deal-feature-item">
              <span style="color: var(--gold);">&#10003;</span>
              <span>Includes free laser engraving on all 3 bottles</span>
            </div>
            <div class="deal-feature-item">
              <span style="color: var(--gold);">&#10003;</span>
              <span>Complimentary luxury wooden presentation chest</span>
            </div>
          </div>
          <div class="coupon-code-pill" onclick="copyCouponCode('MYOP3FOR2')">
            <span>USE COUPON:</span>
            <span class="code-text" id="coupon-1-text">MYOP3FOR2</span>
            <span class="copy-hint" id="coupon-1-hint">Click to Copy</span>
          </div>
          <button class="primary-btn" style="width: 100%;" onclick="applyDealToCart('MYOP3FOR2')">
            Apply Deal &amp; Shop 3 Bottles &rarr;
          </button>
        </div>

        <!-- Deal 2 -->
        <div class="deal-card">
          <div class="deal-badge-pill">HIS &amp; HERS</div>
          <h3 class="deal-title">Couple's Personalised Set</h3>
          <p class="deal-desc">
            Two bespoke 100ml flacons created in harmonic polarity—one nocturnal and woody, one velvety and floral. Both engraved with your wedding or anniversary date.
          </p>
          <div class="deal-features">
            <div class="deal-feature-item">
              <span style="color: var(--gold);">&#10003;</span>
              <span>100ml Éternel Noir + 100ml Rose Royale</span>
            </div>
            <div class="deal-feature-item">
              <span style="color: var(--gold);">&#10003;</span>
              <span>Custom matching laser engravings included</span>
            </div>
            <div class="deal-feature-item">
              <span style="color: var(--gold);">&#10003;</span>
              <span>Save ₹4,500 compared to individual bottles</span>
            </div>
          </div>
          <div class="deal-price-block">
            <span class="deal-price-val">₹19,999</span>
            <span class="deal-orig-val">₹24,498</span>
          </div>
          <button class="primary-btn" style="width: 100%;" onclick="addBundleToBag('Couple\'s Personalised Set', 19999, '/elixora_rose_bottle.jpg')">
            ✦ Add Couple's Set to Bag
          </button>
        </div>

        <!-- Deal 3 -->
        <div class="deal-card">
          <div class="deal-badge-pill">ON-THE-GO LUXURY</div>
          <h3 class="deal-title">Pocket Perfume Trio (3 &times; 20ml)</h3>
          <p class="deal-desc">
            Sleek cylindrical anodized travel atomizers engineered for private jets, evening clutches, and gym bags. 50% high oil concentration that lasts all day.
          </p>
          <div class="deal-features">
            <div class="deal-feature-item">
              <span style="color: var(--gold);">&#10003;</span>
              <span>3 &times; 20ml aircraft-grade travel atomizers</span>
            </div>
            <div class="deal-feature-item">
              <span style="color: var(--gold);">&#10003;</span>
              <span>Pre-filled with Midnight Oud, Aqua, and Vanille</span>
            </div>
            <div class="deal-feature-item">
              <span style="color: var(--gold);">&#10003;</span>
              <span>Includes stainless steel refilling funnel</span>
            </div>
          </div>
          <div class="deal-price-block">
            <span class="deal-price-val">₹1,799</span>
            <span class="deal-orig-val">₹2,999</span>
          </div>
          <button class="primary-btn" style="width: 100%;" onclick="addBundleToBag('Pocket Perfume Trio (3x20ml)', 1799, '/elixora_hero_bottle.jpg')">
            ✦ Add Travel Trio to Bag
          </button>
        </div>
      </div>
    </section>

    <!-- 4. Seasonal Fragrances Section -->
    <section class="section-container" id="seasonal">
      <div class="section-header centered">
        <span class="section-eyebrow">EPHEMERAL HARMONIES</span>
        <h2 class="section-title">Scents of the Season</h2>
        <p class="section-subtitle">
          Nature shifts its temperature; allow your fragrance to mirror the season. Each season unveils 5 distinct, exclusive ÉLIXORA creations with zero repetition across the year.
        </p>
      </div>

      <div class="seasonal-tabs" id="seasonal-tabs">
        <button class="seasonal-tab-btn active" data-season="autumn">🍂 Autumn</button>
        <button class="seasonal-tab-btn" data-season="winter">❄️ Winter</button>
        <button class="seasonal-tab-btn" data-season="spring">🌸 Spring</button>
        <button class="seasonal-tab-btn" data-season="summer">☀️ Summer</button>
      </div>

      <div id="seasonal-desc-content" class="seasonal-desc-content" style="max-width: 820px; margin: 0 auto 2.5rem; text-align: center;"></div>

      <div class="products-grid" id="seasonal-products-grid">
        <!-- Filtered seasonal products -->
      </div>
    </section>

    <!-- 5. Fragrance Mood Section (Horizontal) -->
    <section class="section-container" id="moods" style="background: rgba(255, 255, 255, 0.015);">
      <div class="section-header centered">
        <span class="section-eyebrow">YOUR MOOD &middot; YOUR SCENT</span>
        <h2 class="section-title">Emotional Alchemy</h2>
        <p class="section-subtitle">
          A single spritz transforms presence. Choose the mood you wish to inhabit today.
        </p>
      </div>

      <div class="mood-cards-container">
        <div class="mood-card" onclick="filterCatalogBy('FLORAL')">
          <div class="mood-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
          </div>
          <span class="mood-feel">Feeling</span>
          <h3 class="mood-name">ROMANTIC</h3>
          <span class="mood-arrow">&darr;</span>
          <p class="mood-scent-notes">Rose Damascena / Bourbon Vanilla</p>
        </div>

        <div class="mood-card" onclick="filterCatalogBy('WOODY')">
          <div class="mood-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
          </div>
          <span class="mood-feel">Feeling</span>
          <h3 class="mood-name">CONFIDENT</h3>
          <span class="mood-arrow">&darr;</span>
          <p class="mood-scent-notes">Smoked Oud / Tuscan Leather</p>
        </div>

        <div class="mood-card" onclick="filterCatalogBy('FRESH')">
          <div class="mood-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>
          </div>
          <span class="mood-feel">Feeling</span>
          <h3 class="mood-name">FRESH</h3>
          <span class="mood-arrow">&darr;</span>
          <p class="mood-scent-notes">Calabrian Bergamot / Ocean Sea Salt</p>
        </div>

        <div class="mood-card" onclick="filterCatalogBy('ORIENTAL')">
          <div class="mood-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
          </div>
          <span class="mood-feel">Feeling</span>
          <h3 class="mood-name">MYSTERIOUS</h3>
          <span class="mood-arrow">&darr;</span>
          <p class="mood-scent-notes">Dark Amber / Smoked Incense</p>
        </div>

        <div class="mood-card" onclick="filterCatalogBy('WOODY')">
          <div class="mood-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/></svg>
          </div>
          <span class="mood-feel">Feeling</span>
          <h3 class="mood-name">CALM</h3>
          <span class="mood-arrow">&darr;</span>
          <p class="mood-scent-notes">French Lavender / White Sandalwood</p>
        </div>
      </div>
    </section>

    <!-- ==========================================================
         MYOP PERFUME BAR STORE LOCATOR (68+ STORES NATIONWIDE)
         ========================================================== -->
    <section class="store-locator-section" id="stores">
      <div class="section-header centered">
        <span class="section-eyebrow">INDIA'S EXCLUSIVE PERFUME BARS &middot; 5 FLAGSHIP LOCATIONS</span>
        <h2 class="section-title">Experience Our Perfume Bars</h2>
        <p class="section-subtitle">
          Touch, smell, and formulate your personal scent in real time. Our master perfumers blend your 50% tropical oil formulation right before your eyes, accompanied by instant 5-minute complimentary laser engraving.
        </p>
      </div>

      <!-- City Navigation Filter Tabs (5 Key Flagships) -->
      <div class="store-filters-bar">
        <button class="store-filter-btn active" onclick="filterStoresByCity('all', this)">All Stores (5)</button>
        <button class="store-filter-btn" onclick="filterStoresByCity('Mumbai', this)">Mumbai</button>
        <button class="store-filter-btn" onclick="filterStoresByCity('Delhi NCR', this)">Delhi NCR</button>
        <button class="store-filter-btn" onclick="filterStoresByCity('Bengaluru', this)">Bengaluru</button>
        <button class="store-filter-btn" onclick="filterStoresByCity('Kochi', this)">Kochi</button>
        <button class="store-filter-btn" onclick="filterStoresByCity('Chennai', this)">Chennai</button>
      </div>

      <!-- Live Search Box for Stores -->
      <div style="max-width: 460px; margin: 0 auto 2.5rem auto;">
        <input type="text" class="custom-text-input" id="store-search-input" placeholder="Search mall name, locality, or city..." oninput="handleStoreSearch(this.value)" style="text-align: center;" />
      </div>

      <!-- Stores Cards Grid -->
      <div class="stores-grid" id="stores-container">
        <!-- Store 1: Mumbai -->
        <div class="store-card" data-city="Mumbai" data-name="Phoenix Palladium Mumbai">
          <div class="store-card-city">MUMBAI &middot; MAHARASHTRA</div>
          <h3 class="store-card-name">Phoenix Palladium Flagship Bar</h3>
          <p class="store-card-mall">Level 2, Luxury Concourse, High Street Phoenix, Lower Parel, Mumbai 400013</p>
          <div class="store-card-hours">Open Daily: 10:30 AM &ndash; 10:00 PM &middot; +91 (022) 6940-2026</div>
          <div class="store-amenities-row">
            <span class="amenity-chip">&#10003; Live Blending</span>
            <span class="amenity-chip">&#10003; 5-Min Engraving</span>
            <span class="amenity-chip">&#10003; Eco-Refill</span>
          </div>
          <div class="store-card-actions">
            <a href="https://maps.google.com/?q=Phoenix+Palladium+Mumbai" target="_blank" rel="noopener" class="secondary-btn" style="padding: 8px 14px; font-size: 0.75rem; text-decoration: none;">
              Get Directions &rarr;
            </a>
            <button class="primary-btn" style="padding: 8px 14px; font-size: 0.75rem;" onclick="openBookStoreModal('Phoenix Palladium Flagship Bar, Mumbai')">
              Book Blending Session
            </button>
          </div>
        </div>

        <!-- Store 2: Delhi -->
        <div class="store-card" data-city="Delhi NCR" data-name="Select CITYWALK New Delhi">
          <div class="store-card-city">NEW DELHI &middot; NCR</div>
          <h3 class="store-card-name">Select CITYWALK Perfume Bar</h3>
          <p class="store-card-mall">Ground Floor, Central Atrium, Saket District Centre, New Delhi 110017</p>
          <div class="store-card-hours">Open Daily: 10:00 AM &ndash; 10:00 PM &middot; +91 (011) 4892-1980</div>
          <div class="store-amenities-row">
            <span class="amenity-chip">&#10003; Live Blending</span>
            <span class="amenity-chip">&#10003; 5-Min Engraving</span>
            <span class="amenity-chip">&#10003; Eco-Refill</span>
          </div>
          <div class="store-card-actions">
            <a href="https://maps.google.com/?q=Select+Citywalk+Saket+Delhi" target="_blank" rel="noopener" class="secondary-btn" style="padding: 8px 14px; font-size: 0.75rem; text-decoration: none;">
              Get Directions &rarr;
            </a>
            <button class="primary-btn" style="padding: 8px 14px; font-size: 0.75rem;" onclick="openBookStoreModal('Select CITYWALK Perfume Bar, New Delhi')">
              Book Blending Session
            </button>
          </div>
        </div>

        <!-- Store 3: Bengaluru -->
        <div class="store-card" data-city="Bengaluru" data-name="Phoenix Marketcity Bengaluru">
          <div class="store-card-city">BENGALURU &middot; KARNATAKA</div>
          <h3 class="store-card-name">Phoenix Marketcity Perfume Lounge</h3>
          <p class="store-card-mall">Upper Ground Floor, Dyavasandra Industrial Area, Whitefield Road, Bengaluru 560048</p>
          <div class="store-card-hours">Open Daily: 10:30 AM &ndash; 10:00 PM &middot; +91 (080) 6122-3400</div>
          <div class="store-amenities-row">
            <span class="amenity-chip">&#10003; Live Blending</span>
            <span class="amenity-chip">&#10003; 5-Min Engraving</span>
            <span class="amenity-chip">&#10003; Eco-Refill</span>
          </div>
          <div class="store-card-actions">
            <a href="https://maps.google.com/?q=Phoenix+Marketcity+Whitefield+Bangalore" target="_blank" rel="noopener" class="secondary-btn" style="padding: 8px 14px; font-size: 0.75rem; text-decoration: none;">
              Get Directions &rarr;
            </a>
            <button class="primary-btn" style="padding: 8px 14px; font-size: 0.75rem;" onclick="openBookStoreModal('Phoenix Marketcity, Bengaluru')">
              Book Blending Session
            </button>
          </div>
        </div>

        <!-- Store 4: Kochi -->
        <div class="store-card" data-city="Kochi" data-name="Lulu Mall Flagship 01 Kochi">
          <div class="store-card-city">KOCHI &middot; KERALA</div>
          <h3 class="store-card-name">Lulu International Mall (Flagship #01)</h3>
          <p class="store-card-mall">Level 1, Center Wing, Edappally Toll Junction, Kochi, Kerala 682024</p>
          <div class="store-card-hours">Open Daily: 10:00 AM &ndash; 10:30 PM &middot; +91 (0484) 272-8000</div>
          <div class="store-amenities-row">
            <span class="amenity-chip">&#10003; India's 1st Perfume Bar</span>
            <span class="amenity-chip">&#10003; Live Blending</span>
            <span class="amenity-chip">&#10003; Laser Engraving</span>
          </div>
          <div class="store-card-actions">
            <a href="https://maps.google.com/?q=Lulu+Mall+Kochi" target="_blank" rel="noopener" class="secondary-btn" style="padding: 8px 14px; font-size: 0.75rem; text-decoration: none;">
              Get Directions &rarr;
            </a>
            <button class="primary-btn" style="padding: 8px 14px; font-size: 0.75rem;" onclick="openBookStoreModal('Lulu Mall Flagship #01, Kochi')">
              Book Blending Session
            </button>
          </div>
        </div>

        <!-- Store 5: Chennai -->
        <div class="store-card" data-city="Chennai" data-name="Express Avenue Mall Chennai">
          <div class="store-card-city">CHENNAI &middot; TAMIL NADU</div>
          <h3 class="store-card-name">Express Avenue Perfume Bar</h3>
          <p class="store-card-mall">Central Mall Ground Floor, Whites Road, Royapettah, Chennai 600014</p>
          <div class="store-card-hours">Open Daily: 10:30 AM &ndash; 10:00 PM &middot; +91 (044) 2846-4646</div>
          <div class="store-amenities-row">
            <span class="amenity-chip">&#10003; Live Blending</span>
            <span class="amenity-chip">&#10003; 5-Min Engraving</span>
            <span class="amenity-chip">&#10003; Eco-Refill</span>
          </div>
          <div class="store-card-actions">
            <a href="https://maps.google.com/?q=Express+Avenue+Chennai" target="_blank" rel="noopener" class="secondary-btn" style="padding: 8px 14px; font-size: 0.75rem; text-decoration: none;">
              Get Directions &rarr;
            </a>
            <button class="primary-btn" style="padding: 8px 14px; font-size: 0.75rem;" onclick="openBookStoreModal('Express Avenue Perfume Bar, Chennai')">
              Book Blending Session
            </button>
          </div>
        </div>


      </div>
    </section>

    <!-- 7. The Art of Ingredients -->
    <section class="section-container" id="ingredients">
      <div class="section-header centered">
        <span class="section-eyebrow">RAW BOTANICAL HARVEST</span>
        <h2 class="section-title">The Art of Ingredients</h2>
        <p class="section-subtitle">
          Sourced ethically from historic soils. Pure essences preserved with artisan distillation methods.
        </p>
      </div>

      <div class="ingredients-grid">
        <div class="ingredient-card" onmouseenter="previewIngredientTheme('rose')">
          <span class="ingredient-origin">Grasse, France</span>
          <h3 class="ingredient-name">ROSE CENTIFOLIA</h3>
          <p class="ingredient-desc">Harvested exclusively at dawn in May. Delivers an intoxicating, honeyed velvety nectar.</p>
        </div>
        <div class="ingredient-card" onmouseenter="previewIngredientTheme('oud')">
          <span class="ingredient-origin">Assam, India</span>
          <h3 class="ingredient-name">ROYAL OUD</h3>
          <p class="ingredient-desc">Aged agarwood distilled with patience to extract deep, smoky, balsamic wood resins.</p>
        </div>
        <div class="ingredient-card" onmouseenter="previewIngredientTheme('aqua')">
          <span class="ingredient-origin">Calabria, Italy</span>
          <h3 class="ingredient-name">BERGAMOT</h3>
          <p class="ingredient-desc">Cold-pressed citrus peel delivering crisp, sun-drenched aromatic effervescence.</p>
        </div>
        <div class="ingredient-card" onmouseenter="previewIngredientTheme('noir')">
          <span class="ingredient-origin">Kashmir, India</span>
          <h3 class="ingredient-name">KASHMIRI SAFFRON</h3>
          <p class="ingredient-desc">Rare crimson threads providing metallic, bittersweet leather facets and intense golden warmth.</p>
        </div>
        <div class="ingredient-card" onmouseenter="previewIngredientTheme('rose')">
          <span class="ingredient-origin">Madurai, India</span>
          <h3 class="ingredient-name">JASMINE SAMBAC</h3>
          <p class="ingredient-desc">Luminous white floral blossom possessing hypnotic sweetness and nocturnal animalic charm.</p>
        </div>
        <div class="ingredient-card" onmouseenter="previewIngredientTheme('oud')">
          <span class="ingredient-origin">Mysore, India</span>
          <h3 class="ingredient-name">SANDALWOOD</h3>
          <p class="ingredient-desc">Creamy, sacred timber providing serene spiritual depth and an everlasting drydown.</p>
        </div>
        <div class="ingredient-card" onmouseenter="previewIngredientTheme('oud')">
          <span class="ingredient-origin">Baltic Coast</span>
          <h3 class="ingredient-name">FOSSIL AMBER</h3>
          <p class="ingredient-desc">Fossilized coniferous tree resin yielding golden, balsamic, honey-tobacco warmth.</p>
        </div>
        <div class="ingredient-card" onmouseenter="previewIngredientTheme('aqua')">
          <span class="ingredient-origin">Alpine Meadows</span>
          <h3 class="ingredient-name">WHITE MUSK</h3>
          <p class="ingredient-desc">Cruelty-free botanical molecules that replicate skin-warmed silk and comforting clean aura.</p>
        </div>
      </div>
    </section>

    <!-- ==========================================================
         ECO-REFILL & SUSTAINABILITY PROGRAM
         ========================================================== -->
    

    <!-- ==========================================================
         CORPORATE GIFTING & BESPOKE WEDDING FAVORS
         ========================================================== -->
    

    <!-- 8. Luxury Brands Marquee -->
    

    <!-- 9. Editorial Story Section -->
    <section class="story-section" id="story">
      <div class="story-img-frame">
        <img src="/elixora_hero_bottle.jpg" alt="ÉLIXORA Haute Craftsmanship" />
      </div>
      <div class="story-content">
        <span class="section-eyebrow">OUR PHILOSOPHY</span>
        <h2 class="story-quote">
          &ldquo;More than a fragrance. A scent becomes the architecture of the moments you remember.&rdquo;
        </h2>
        <p class="story-text">
          Every ÉLIXORA flacon is conceived as an architectural monument to fleeting beauty. Hand-blown cut crystal, 24k electroplated collars, and precious botanical extractions aged in darkness until perfect equilibrium is unlocked.
        </p>
        <p class="story-text">
          We invite you into an intimate dialogue between emotion and aroma. Where your presence speaks before a single word is spoken.
        </p>
        <a href="#catalog" class="secondary-btn">
          Explore the Archive &rarr;
        </a>
      </div>
    </section>

    <!-- 10. Reviews & Testimonials Carousel -->
    <section class="section-container" id="reviews" style="background: rgba(255, 255, 255, 0.01);">
      <div class="section-header centered">
        <span class="section-eyebrow">VOICES OF CONNOISSEURS</span>
        <h2 class="section-title">The Impression</h2>
      </div>

      <div class="testimonials-wrap">
        <div class="testimonial-slide active" data-slide="0">
          <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <blockquote class="testimonial-quote">
            &ldquo;Éternel Noir is poetry in glass. The iris suspended in smoked amber leaves a lingering trail that colleagues and strangers ask about constantly.&rdquo;
          </blockquote>
          <div class="testimonial-author">Aanya Malhotra</div>
          <div class="testimonial-verified">Verified Collector &middot; Mumbai</div>
        </div>

        <div class="testimonial-slide" data-slide="1">
          <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <blockquote class="testimonial-quote">
            &ldquo;The bottle alone belongs in the Louvre. When you hold the heavy multifaceted crystal and spray the first mist, you realize what real luxury feels like.&rdquo;
          </blockquote>
          <div class="testimonial-author">Julian Von Habsburg</div>
          <div class="testimonial-verified">Verified Collector &middot; Zurich</div>
        </div>

        <div class="testimonial-slide" data-slide="2">
          <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <blockquote class="testimonial-quote">
            &ldquo;Midnight Oud has an extraordinary 18-hour longevity without any harsh edges. Pure honeyed balsamic wood that evolves like a vintage melody.&rdquo;
          </blockquote>
          <div class="testimonial-author">Elena Rostova</div>
          <div class="testimonial-verified">Verified Collector &middot; Paris</div>
        </div>

        <div class="testimonial-controls">
          <button class="carousel-nav-btn" onclick="prevTestimonial()" aria-label="Previous Review">&larr;</button>
          <button class="carousel-nav-btn" onclick="nextTestimonial()" aria-label="Next Review">&rarr;</button>
        </div>
      </div>
    </section>
  </main>

  <!-- Luxury Footer -->
  <footer class="footer">
    <div class="footer-top-grid">
      <div class="footer-brand-col">
        <div class="brand-title">ÉLIXORA</div>
        <div class="brand-sub">THE ART OF FRAGRANCE</div>
        <p>
          Haute Parfumerie and bespoke olfactory design. Handcrafted crystal bottles filled with the rarest botanical extractions.
        </p>
      </div>

      <div>
        <h4 class="footer-col-heading">PERFUME BAR &amp; ATELIER</h4>
        <ul class="footer-links-list">
          <li><a href="#myop-studio" style="color: var(--gold);">✦ Make Your Own Perfume</a></li>
          <li><a href="#discovery">Discovery Sets (100% Cash-Back)</a></li>
          <li><a href="#deals">Scent Deals &amp; Combos</a></li>
          <li><a href="#stores">5 Flagship Stores Across India</a></li>
                            </ul>
      </div>

      <div>
        <h4 class="footer-col-heading">COLLECTIONS</h4>
        <ul class="footer-links-list">
          <li><a href="#catalog" onclick="filterCatalogBy('ALL')">All Fragrances</a></li>
          <li><a href="#collections">Explore by Fragrance Family</a></li>
          <li><a href="#seasonal">Seasonal Releases</a></li>
          <li><a href="#ingredients">Rare Botanical Harvest</a></li>
          <li><a href="#story">Our Philosophy</a></li>
        </ul>
      </div>

      <div>
        <h4 class="footer-col-heading">CONCIERGE &amp; TRACKING</h4>
        <ul class="footer-links-list">
          <li><a href="javascript:void(0)" onclick="openTrackOrderModal()" style="color: var(--gold-light);">📦 Track Your Order</a></li>
          <li><a href="#stores" onclick="openBookStoreModal('Flagship Perfume Bar')">Book 1-on-1 Blending Session</a></li>
          <li><a href="#footer" onclick="showToast('Free Express Shipping across India')">Express Shipping Policy</a></li>
          <li><a href="#footer" onclick="showToast('50% European Oil Certificate included with every order')">Authenticity &amp; Oil Guarantee</a></li>
          <li><a href="#footer" onclick="showToast('Support: concierge@elixora-fragrances.com · WhatsApp: +91 98765 43210')">Customer Support</a></li>
        </ul>
      </div>

      <div>
        <h4 class="footer-col-heading">JOIN THE ÉLIXORA WORLD</h4>
        <p style="color: var(--muted-color); font-size: 0.85rem; margin-bottom: 1rem;">
          Receive private invitations to limited harvest bottlings and private salon gatherings.
        </p>
        <form class="newsletter-form" onsubmit="handleNewsletter(event)">
          <input type="email" class="newsletter-input" placeholder="Your private email" required />
          <button type="submit" class="newsletter-submit-btn" aria-label="Subscribe">&rarr;</button>
        </form>
      </div>
    </div>

    <div class="footer-bottom-row">
      <span>&copy; 2026 ÉLIXORA Haute Parfumerie. Crafted for unforgettable memories.</span>
      <span>Grasse &middot; Paris &middot; London &middot; New York &middot; Tokyo</span>
    </div>
  </footer>

  <!-- Slide-out Cart Drawer -->
  <div class="drawer-overlay" id="cart-drawer-overlay" onclick="closeCartDrawer()"></div>
  <aside class="drawer-panel" id="cart-drawer-panel" aria-label="Shopping Bag Drawer">
    <div class="drawer-header">
      <h3 class="drawer-title">YOUR BAG</h3>
      <button class="close-drawer-btn" onclick="closeCartDrawer()">&times;</button>
    </div>

    <!-- Free Shipping / Tropical Oil Progress Notice -->
    <div style="background: rgba(212,175,112,0.08); border-bottom: 1px solid rgba(212,175,112,0.15); padding: 10px 1.5rem; font-size: 0.75rem; color: var(--gold); display: flex; align-items: center; justify-content: space-between;">
      <span>&#10003; Free Express Air Delivery &middot; All India</span>
      <span style="color: #fff;">50% Tropical Oil</span>
    </div>

    <div class="drawer-body" id="cart-items-container">
      <!-- Injected via JS -->
    </div>

    <div class="drawer-footer">
      <!-- Complimentary 2ml Vial Selector for Orders > ₹1,999 -->
      <div class="free-sample-selector" id="free-sample-container">
        <span class="free-sample-title">✦ COMPLIMENTARY 2ML VIAL WITH YOUR ORDER</span>
        <select class="free-sample-select" id="cart-free-sample-select">
          <option value="Éternel Noir 2ml">Complimentary: 2ml Éternel Noir (Extrait)</option>
          <option value="Rose Royale 2ml">Complimentary: 2ml Rose Royale (EDP)</option>
          <option value="Midnight Oud 2ml">Complimentary: 2ml Midnight Oud (EDP)</option>
          <option value="Aqua Céleste 2ml">Complimentary: 2ml Aqua Céleste (Parfum)</option>
          <option value="Velvet Vanille 2ml">Complimentary: 2ml Velvet Vanille (Extrait)</option>
        </select>
      </div>

      <!-- Pincode Delivery Estimator -->
      <div class="cart-pincode-box">
        <div class="pincode-input-group">
          <input type="text" class="pincode-input" id="cart-pincode-input" placeholder="Enter 6-digit Pincode" maxlength="6" />
          <button class="pincode-check-btn" onclick="checkCartPincode()">Check</button>
        </div>
        <div class="pincode-result" id="cart-pincode-result"></div>
      </div>

      <!-- Coupon / Voucher Code Input -->
      <div class="cart-coupon-box">
        <div class="coupon-input-group">
          <input type="text" class="coupon-input" id="cart-coupon-input" placeholder="Coupon (e.g. MYOP3FOR2, WELCOME10)" />
          <button class="coupon-apply-btn" onclick="applyCartCoupon()">Apply</button>
        </div>
        <div class="coupon-result-badge" id="cart-coupon-result"></div>
      </div>

      <!-- Price Breakdown -->
      <div class="subtotal-row">
        <span class="subtotal-label">Subtotal</span>
        <span class="subtotal-value" id="cart-subtotal-val">₹0</span>
      </div>

      <div class="subtotal-row" id="cart-discount-row" style="display: none;">
        <span class="subtotal-label" style="color: #4ade80;">Coupon Discount</span>
        <span class="subtotal-value" id="cart-discount-val" style="color: #4ade80;">-₹0</span>
      </div>

      <div class="subtotal-row">
        <span class="subtotal-label">Express Delivery (All India)</span>
        <span class="subtotal-value" style="color: var(--gold); font-size: 0.85rem;">FREE</span>
      </div>

      <div class="subtotal-row" style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 8px; margin-top: 6px;">
        <span class="subtotal-label" style="font-weight: 700; color: #fff;">Estimated Total</span>
        <span class="subtotal-value" id="cart-final-total-val" style="font-size: 1.25rem; color: var(--gold); font-weight: 700;">₹0</span>
      </div>

      <button class="checkout-btn" onclick="proceedToCheckout()">
        SECURE CHECKOUT &rarr;
      </button>

      <div style="display: flex; justify-content: center; gap: 15px; margin-top: 10px; font-size: 0.7rem; color: var(--muted-color);">
        <span>&#128274; 256-Bit SSL</span>
        <span>&#128179; UPI / Cards / NetBanking</span>
        <span>&#128666; Express Air</span>
      </div>
    </div>
  </aside>

  <!-- Slide-out Wishlist Drawer -->
  <div class="drawer-overlay" id="wishlist-drawer-overlay" onclick="closeWishlistDrawer()"></div>
  <aside class="drawer-panel" id="wishlist-drawer-panel" aria-label="Saved Fragrances Drawer">
    <div class="drawer-header">
      <h3 class="drawer-title">SAVED ELIXIRS</h3>
      <button class="close-drawer-btn" onclick="closeWishlistDrawer()">&times;</button>
    </div>
    <div class="drawer-body" id="wishlist-items-container">
      <!-- Injected via JS -->
    </div>
  </aside>

  <!-- Fullscreen Product Detail Modal (with Fragrance Pyramid & Personalisation) -->
  <div class="product-modal-backdrop" id="product-detail-modal" onclick="closeProductModalOnBackdrop(event)">
    <div class="product-modal-card">
      <button class="modal-close-btn" onclick="closeProductModal()">&times;</button>
      <div class="modal-gallery-side">
        <img class="modal-main-img" id="modal-product-img" src="/elixora_hero_bottle.jpg" alt="Fragrance Flacon" />
      </div>
      <div class="modal-content-side">
        <span class="modal-brand" id="modal-brand-label">ÉLIXORA</span>
        <h2 class="modal-title" id="modal-title-label">ÉTERNEL NOIR</h2>
        <div class="modal-rating-row">
          <span style="color: var(--gold);" id="modal-rating-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
          <span style="font-size: 0.8rem; color: var(--muted-color); font-family: var(--nav-font);" id="modal-reviews-count">(48 Connoisseur Reviews)</span>
        </div>
        <div class="modal-price" id="modal-price-label">₹12,999</div>
        <p class="modal-desc" id="modal-desc-label">
          A nocturnal tour-de-force inspired by moonlit crystal facets. Velveteen iris and smoked wood resins suspended in pure clarity.
        </p>

        <!-- Concentration Selector -->
        <div class="variant-group">
          <span class="variant-label">Concentration (50% Tropical Oil Available)</span>
          <div class="variant-pills-row" id="modal-concentration-pills">
            <button class="variant-pill" onclick="selectConcentration('EDT', 0.8)">EDT (15%)</button>
            <button class="variant-pill active" onclick="selectConcentration('EDP', 1.0)">EDP (25%)</button>
            <button class="variant-pill" onclick="selectConcentration('Parfum', 1.25)">Parfum (35%)</button>
            <button class="variant-pill" onclick="selectConcentration('Extrait', 1.5)">Extrait (50% Oil)</button>
          </div>
        </div>

        <!-- Size Selector -->
        <div class="variant-group">
          <span class="variant-label">Flacon Size</span>
          <div class="variant-pills-row" id="modal-size-pills">
            <button class="variant-pill" onclick="selectSize('30ml', 0.6)">30ml Travel</button>
            <button class="variant-pill" onclick="selectSize('50ml', 0.8)">50ml Flacon</button>
            <button class="variant-pill active" onclick="selectSize('100ml', 1.0)">100ml Grand</button>
            <button class="variant-pill" onclick="selectSize('150ml', 1.4)">150ml Decanter</button>
          </div>
        </div>

        <!-- Complimentary Laser Engraving Option on Product -->
        <div class="modal-engrave-toggle-wrap">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
            <label style="display: flex; align-items: center; gap: 8px; cursor: pointer; font-size: 0.82rem; color: #fff;">
              <input type="checkbox" id="modal-engrave-checkbox" onchange="toggleModalEngraveInput(this.checked)" />
              <span>✦ Add Complimentary Laser Engraving (Free)</span>
            </label>
            <span style="font-size: 0.7rem; color: var(--gold);">5-Min Laser</span>
          </div>
          <div id="modal-engrave-input-container" style="display: none; margin-top: 8px;">
            <input type="text" class="custom-text-input" id="modal-engrave-input-text" maxlength="20" placeholder="Enter Name or Date to Engrave (e.g. ARJUN 2026)" style="font-size: 0.8rem; padding: 8px 12px;" />
          </div>
        </div>

        <!-- Fragrance Pyramid -->
        <div class="pyramid-container">
          <span class="pyramid-heading">&#10022; THE OLFACTORY PYRAMID &#10022;</span>
          <div class="pyramid-tier">
            <span class="tier-label">TOP NOTES</span>
            <span class="tier-notes" id="modal-top-notes">Black Pepper &middot; Blue Iris &middot; Bergamot</span>
          </div>
          <div class="pyramid-tier">
            <span class="tier-label">HEART NOTES</span>
            <span class="tier-notes" id="modal-heart-notes">Smoked Amber &middot; Incense &middot; Rose</span>
          </div>
          <div class="pyramid-tier">
            <span class="tier-label">BASE NOTES</span>
            <span class="tier-notes" id="modal-base-notes">Aged Oud &middot; Vetiver &middot; Cashmere Musk</span>
          </div>
        </div>

        <div class="modal-actions-row">
          <button class="modal-add-bag-btn" id="modal-add-bag-btn" onclick="addActiveModalToBag()">
            ADD TO BAG &middot; <span id="modal-btn-price">₹12,999</span>
          </button>
          <button class="modal-wish-btn" id="modal-wish-btn" onclick="toggleActiveModalWishlist()">
            &hearts; SAVE
          </button>
        </div>

        <button class="modal-compare-action-btn" onclick="addActiveModalToCompare()">
          ⚖ Compare with Another Fragrance
        </button>
      </div>
    </div>
  </div>

  <!-- Track Order Modal -->
  <div class="track-order-modal-backdrop" id="track-order-modal" onclick="closeTrackOrderModalOnBackdrop(event)">
    <div class="track-order-card">
      <button class="modal-close-btn" onclick="closeTrackOrderModal()">&times;</button>
      <div style="text-align: center; margin-bottom: 1.5rem;">
        <span class="section-eyebrow">BLUE DART &middot; CONCIERGE AIR</span>
        <h3 style="font-family: var(--heading-font); font-size: 1.5rem; color: #fff; margin: 6px 0;">
          Track Your Perfume Order
        </h3>
        <p style="font-size: 0.8rem; color: var(--muted-color);">
          Enter your 9-digit Order ID or 10-digit registered mobile number.
        </p>
      </div>

      <form onsubmit="handleTrackOrderSubmit(event)" style="margin-bottom: 1.5rem;">
        <div style="display: flex; gap: 8px;">
          <input type="text" class="custom-text-input" id="track-order-input" placeholder="e.g. ELX-94829 or 9876543210" required />
          <button type="submit" class="primary-btn" style="white-space: nowrap; padding: 0 18px;">
            Track &rarr;
          </button>
        </div>
      </form>

      <!-- Live Simulated Stepper -->
      <div id="tracking-result-box" style="display: none;">
        <div class="track-info-header">
          <div>
            <span style="font-size: 0.7rem; color: var(--muted-color); text-transform: uppercase;">Tracking Number:</span>
            <div style="color: var(--gold); font-family: monospace; font-size: 0.95rem; font-weight: 700;" id="track-awb-num">BLUEDART-AIR-7492041</div>
          </div>
          <div style="text-align: right;">
            <span style="font-size: 0.7rem; color: var(--muted-color); text-transform: uppercase;">Estimated Delivery:</span>
            <div style="color: #4ade80; font-size: 0.85rem; font-weight: 600;" id="track-eta-date">Tomorrow by 2:00 PM</div>
          </div>
        </div>

        <div class="track-timeline">
          <div class="timeline-node complete">
            <div class="timeline-dot">&#10003;</div>
            <div class="timeline-info">
              <h4>Order Received &amp; Verified</h4>
              <p>Formulation specifications dispatched to Master Perfumer Atelier.</p>
              <span class="timeline-time">Yesterday, 4:15 PM</span>
            </div>
          </div>

          <div class="timeline-node complete">
            <div class="timeline-dot">&#10003;</div>
            <div class="timeline-info">
              <h4>Hand-Blended with 50% Tropical Oil</h4>
              <p>Formula compounded with authentic Grasse botanical essences. Passed chromatography quality control.</p>
              <span class="timeline-time">Today, 9:30 AM</span>
            </div>
          </div>

          <div class="timeline-node complete">
            <div class="timeline-dot">&#10003;</div>
            <div class="timeline-info">
              <h4>High-Precision Laser Engraving Applied</h4>
              <p>Crystal flacon custom etched and encased in gold-foiled presentation coffret.</p>
              <span class="timeline-time">Today, 1:45 PM</span>
            </div>
          </div>

          <div class="timeline-node active">
            <div class="timeline-dot">&#9889;</div>
            <div class="timeline-info">
              <h4>Dispatched via BlueDart Priority Air</h4>
              <p>En route from Mumbai Central Distribution Hub to destination city.</p>
              <span class="timeline-time">Today, 5:20 PM &middot; In Transit</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Book Perfume Bar Appointment Modal -->
  <div class="book-store-modal-backdrop" id="book-store-modal" onclick="closeBookStoreModalOnBackdrop(event)">
    <div class="book-store-card">
      <button class="modal-close-btn" onclick="closeBookStoreModal()">&times;</button>
      <div style="text-align: center; margin-bottom: 1.5rem;">
        <span class="section-eyebrow">1-ON-1 BESPOKE SESSION</span>
        <h3 style="font-family: var(--heading-font); font-size: 1.4rem; color: #fff; margin: 6px 0;">
          Reserve a Perfume Bar Appointment
        </h3>
        <p style="font-size: 0.8rem; color: var(--muted-color);">
          Experience a private 30-minute fragrance consultation and live flacon blending with our certified nose.
        </p>
      </div>

      <form onsubmit="handleBookStoreSubmit(event)">
        <div style="margin-bottom: 12px;">
          <label class="custom-field-label" for="booking-store-select">Select Perfume Bar Location:</label>
          <select class="free-sample-select" id="booking-store-select" style="padding: 10px 14px; font-size: 0.88rem;">
            <option value="Phoenix Palladium Flagship Bar, Mumbai">Phoenix Palladium Flagship, Lower Parel, Mumbai</option>
            <option value="Select CITYWALK Perfume Bar, New Delhi">Select CITYWALK, Saket, New Delhi</option>
            <option value="Phoenix Marketcity, Bengaluru">Phoenix Marketcity, Whitefield, Bengaluru</option>
            <option value="Lulu Mall Flagship #01, Kochi">Lulu International Mall (Flagship #01), Kochi</option>
            <option value="Express Avenue Perfume Bar, Chennai">Express Avenue Mall, Royapettah, Chennai</option>
            </select>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 12px;">
          <div>
            <label class="custom-field-label" for="booking-date-input">Preferred Date:</label>
            <input type="date" class="custom-text-input" id="booking-date-input" required style="color: #fff;" />
          </div>
          <div>
            <label class="custom-field-label" for="booking-time-select">Time Slot:</label>
            <select class="free-sample-select" id="booking-time-select" style="padding: 10px 14px; font-size: 0.88rem;">
              <option>11:00 AM &ndash; 11:30 AM</option>
              <option>1:00 PM &ndash; 1:30 PM</option>
              <option>3:30 PM &ndash; 4:00 PM</option>
              <option>5:30 PM &ndash; 6:00 PM</option>
              <option>7:30 PM &ndash; 8:00 PM</option>
            </select>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 16px;">
          <input type="text" class="custom-text-input" id="booking-guest-name" placeholder="Your Full Name" required />
          <input type="tel" class="custom-text-input" id="booking-guest-phone" placeholder="Phone Number" required />
        </div>

        <button type="submit" class="primary-btn" style="width: 100%;">
          Confirm Complimentary Booking &rarr;
        </button>
      </form>
    </div>
  </div>

  <!-- Fullscreen Search Overlay -->
  <div class="search-overlay" id="search-overlay">
    <div class="search-top-bar">
      <span style="font-family: var(--nav-font); letter-spacing: 0.25em; color: var(--gold); font-size: 0.8rem;">SEARCH ÉLIXORA</span>
      <button class="close-drawer-btn" onclick="closeSearchOverlay()">&times;</button>
    </div>
    <div class="search-input-wrap">
      <input type="text" class="search-input-field" id="search-input" placeholder="Search fragrances, notes, brands..." oninput="handleSearchInput(event)" />
    </div>
    <div class="search-popular-tags">
      <span class="search-tag-label">Popular:</span>
      <button class="search-tag-pill" onclick="quickSearch('Oud')">Oud</button>
      <button class="search-tag-pill" onclick="quickSearch('Vanilla')">Vanilla</button>
      <button class="search-tag-pill" onclick="quickSearch('Rose')">Rose</button>
      <button class="search-tag-pill" onclick="quickSearch('Fresh')">Fresh</button>
      <button class="search-tag-pill" onclick="quickSearch('Date Night')">Date Night</button>
      <button class="search-tag-pill" onclick="quickSearch('Unisex')">Unisex</button>
    </div>
    <div class="search-results-grid" id="search-results-grid">
      <!-- Live Search Results -->
    </div>
  </div>

  <!-- Floating Compare Bar (Bottom Docked Tray) -->
  <div class="floating-compare-tray" id="floating-compare-tray">
    <div class="compare-tray-left">
      <span class="compare-tray-title">⚖ COMPARE FRAGRANCES (<span id="compare-tray-count">0</span>/2)</span>
      <span class="compare-tray-subtext">Side-by-side notes, concentration &amp; price</span>
    </div>
    <div class="compare-tray-slots">
      <div class="compare-slot" id="compare-slot-1">
        <span class="compare-slot-placeholder">Select 1st Perfume</span>
      </div>
      <div class="compare-tray-vs">VS</div>
      <div class="compare-slot" id="compare-slot-2">
        <span class="compare-slot-placeholder">Select 2nd Perfume</span>
      </div>
    </div>
    <div class="compare-tray-actions">
      <button class="compare-tray-btn primary" id="compare-now-btn" onclick="openCompareModal()">
        Compare Now &rarr;
      </button>
      <button class="compare-tray-btn clear" onclick="clearComparison()">
        Clear
      </button>
    </div>
  </div>

  <!-- Side-by-Side Perfume Comparison Modal -->
  <div class="compare-modal-backdrop" id="compare-modal" onclick="closeCompareModalOnBackdrop(event)">
    <div class="compare-modal-card">
      <button class="modal-close-btn" onclick="closeCompareModal()" aria-label="Close Comparison">&times;</button>
      
      <div class="compare-modal-header">
        <span class="section-eyebrow">HAUTE PARFUMERIE COMPARISON</span>
        <h2 class="compare-modal-title">Side-by-Side Fragrance Analysis</h2>
        <p class="compare-modal-subtitle">
          Compare olfactory architecture, notes pyramid, tropical oil concentration, and pricing metrics to discover your perfect signature flacon.
        </p>
      </div>

      <!-- Selector Bar to dynamically switch either perfume inside the modal -->
      <div class="compare-select-bar">
        <div class="compare-select-wrapper">
          <label class="compare-select-label" for="compare-select-a">Fragrance A:</label>
          <select class="custom-select compare-perfume-select" id="compare-select-a" onchange="handleCompareDropdownChange(0, this.value)">
            <!-- Populated dynamically with all PRODUCTS -->
          </select>
        </div>

        <button class="compare-swap-btn" onclick="swapCompareItems()" title="Swap Fragrances" aria-label="Swap Products">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M7 16V4M7 4L3 8M7 4L11 8M17 8V20M17 20L21 16M17 20L13 16"/>
          </svg>
          <span>Swap</span>
        </button>

        <div class="compare-select-wrapper">
          <label class="compare-select-label" for="compare-select-b">Fragrance B:</label>
          <select class="custom-select compare-perfume-select" id="compare-select-b" onchange="handleCompareDropdownChange(1, this.value)">
            <!-- Populated dynamically with all PRODUCTS -->
          </select>
        </div>
      </div>

      <!-- Dynamic Side-by-Side Grid Container -->
      <div class="compare-grid" id="compare-grid-content">
        <!-- Rendered dynamically via renderCompareModalContent() in app_js.py -->
      </div>
    </div>
  </div>

  <!-- Toast Notification Box -->
  <div class="toast-notice" id="toast-notice">
    <span style="color: var(--gold);">&#10022;</span>
    <span id="toast-text">Item added to your bag</span>
  </div>

  <!-- =====================================================
       CHECKOUT MODAL
       ===================================================== -->
  <div class="checkout-modal-backdrop" id="checkout-modal" role="dialog" aria-modal="true" aria-label="Checkout">
    <div class="checkout-modal-card">
      <button class="checkout-modal-close" onclick="closeCheckoutModal()" aria-label="Close Checkout">&times;</button>

      <div class="checkout-modal-header">
        <span class="eyebrow">Secure Checkout</span>
        <h2>Complete Your Order</h2>
      </div>

      <div class="checkout-grid">
        <!-- LEFT: Customer Details + Delivery Address -->
        <div>
          <!-- Customer Details -->
          <div class="checkout-section-title">Customer Details</div>

          <div class="checkout-field">
            <label for="co-name">Full Name *</label>
            <input type="text" class="checkout-input" id="co-name" placeholder="e.g. Arjun Sharma" autocomplete="name" />
            <div class="field-error" id="co-name-err">Please enter your full name</div>
          </div>

          <div class="checkout-field">
            <label for="co-mobile">Mobile Number *</label>
            <input type="tel" class="checkout-input" id="co-mobile" placeholder="10-digit mobile number" maxlength="10" autocomplete="tel" />
            <div class="field-error" id="co-mobile-err">Please enter a valid 10-digit mobile number</div>
          </div>

          <div class="checkout-field">
            <label for="co-email">Email Address *</label>
            <input type="email" class="checkout-input" id="co-email" placeholder="your@email.com" autocomplete="email" />
            <div class="field-error" id="co-email-err">Please enter a valid email address</div>
          </div>

          <!-- Delivery Address -->
          <div class="checkout-section-title" style="margin-top: 1.8rem;">Delivery Address</div>

          <div class="checkout-field">
            <label for="co-street">House / Street / Area *</label>
            <input type="text" class="checkout-input" id="co-street" placeholder="e.g. 12A, Rose Garden, MG Road" autocomplete="address-line1" />
            <div class="field-error" id="co-street-err">Please enter your street address</div>
          </div>

          <div class="checkout-field">
            <label for="co-city">City *</label>
            <input type="text" class="checkout-input" id="co-city" placeholder="e.g. Mumbai" autocomplete="address-level2" />
            <div class="field-error" id="co-city-err">Please enter your city</div>
          </div>

          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.8rem;">
            <div class="checkout-field">
              <label for="co-state">State *</label>
              <input type="text" class="checkout-input" id="co-state" placeholder="e.g. Maharashtra" autocomplete="address-level1" />
              <div class="field-error" id="co-state-err">Required</div>
            </div>
            <div class="checkout-field">
              <label for="co-pincode">Pincode *</label>
              <input type="text" class="checkout-input" id="co-pincode" placeholder="6-digit pincode" maxlength="6" autocomplete="postal-code" />
              <div class="field-error" id="co-pincode-err">Invalid pincode</div>
            </div>
          </div>
        </div>

        <!-- RIGHT: Order Summary -->
        <div>
          <div class="checkout-section-title">Order Summary</div>

          <div class="order-summary-box">
            <div id="checkout-order-items">
              <!-- Injected by JS -->
            </div>

            <div class="order-totals">
              <div class="order-total-row">
                <span>Subtotal</span>
                <span id="checkout-subtotal">₹0</span>
              </div>
              <div class="order-total-row" id="checkout-discount-row" style="display:none; color: #4ade80;">
                <span>Discount Applied</span>
                <span id="checkout-discount-val" style="color: #4ade80;">-₹0</span>
              </div>
              <div class="order-total-row">
                <span>Delivery Charge</span>
                <span style="color: var(--gold);">FREE (Express Air)</span>
              </div>
              <div class="order-total-row grand">
                <span>Total Payable</span>
                <span id="checkout-grand-total">₹0</span>
              </div>
            </div>
          </div>

          <!-- Complimentary Vial reminder -->
          <div style="margin-top: 1rem; background: rgba(212,175,112,0.06); border: 1px solid rgba(212,175,112,0.12); border-radius: 10px; padding: 0.8rem 1rem; font-size: 0.75rem; color: var(--gold);">
            ✦ Complimentary 2ml vial included with your order
          </div>

          <button class="checkout-proceed-btn" id="checkout-proceed-btn" onclick="proceedToPayment()">
            PROCEED TO PAYMENT &rarr;
          </button>

          <div style="display: flex; justify-content: center; gap: 14px; margin-top: 1rem; font-size: 0.68rem; color: rgba(255,255,255,0.35);">
            <span>&#128274; 256-Bit SSL</span>
            <span>&#128179; UPI / Cards / COD</span>
            <span>&#128666; Express Air Delivery</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- =====================================================
       PAYMENT MODAL
       ===================================================== -->
  <div class="payment-modal-backdrop" id="payment-modal" role="dialog" aria-modal="true" aria-label="Payment">
    <div class="payment-modal-card">
      <button class="payment-modal-close" onclick="closePaymentModal()" aria-label="Close Payment">&times;</button>

      <h2 class="payment-modal-title">Payment</h2>
      <p class="payment-modal-subtitle">Choose your preferred payment method to complete the order securely.</p>

      <div class="payment-amount-badge">
        <div>
          <div class="label">Amount to Pay</div>
          <div class="amount" id="payment-total-display">₹0</div>
        </div>
        <div style="font-size: 0.7rem; color: var(--muted-color); text-align: right;">
          <div>Free Express Delivery</div>
          <div style="color: var(--gold);">&#10003; Secure & Encrypted</div>
        </div>
      </div>

      <div class="payment-methods-label">Select Payment Method</div>

      <div class="payment-method-options" id="payment-methods-list">
        <!-- UPI -->
        <label class="payment-method-option selected" id="pm-upi-label" onclick="selectPaymentMethod('upi')">
          <input type="radio" name="payment_method" value="upi" checked id="pm-upi" />
          <span class="payment-method-icon">📱</span>
          <div class="payment-method-info">
            <span class="payment-method-name">UPI</span>
            <span class="payment-method-desc">Google Pay, PhonePe, Paytm, BHIM & more</span>
          </div>
        </label>

        <!-- Credit/Debit Card -->
        <label class="payment-method-option" id="pm-card-label" onclick="selectPaymentMethod('card')">
          <input type="radio" name="payment_method" value="card" id="pm-card" />
          <span class="payment-method-icon">💳</span>
          <div class="payment-method-info">
            <span class="payment-method-name">Credit / Debit Card</span>
            <span class="payment-method-desc">Visa, Mastercard, RuPay — all banks accepted</span>
          </div>
        </label>

        <!-- Cash on Delivery -->
        <label class="payment-method-option" id="pm-cod-label" onclick="selectPaymentMethod('cod')">
          <input type="radio" name="payment_method" value="cod" id="pm-cod" />
          <span class="payment-method-icon">💵</span>
          <div class="payment-method-info">
            <span class="payment-method-name">Cash on Delivery</span>
            <span class="payment-method-desc">Pay when your order arrives at your door</span>
          </div>
        </label>
      </div>

      <!-- UPI ID Field (shown for UPI) -->
      <div class="payment-upi-field visible" id="payment-upi-field">
        <label class="checkout-field" style="display:block;">
          <span style="display:block; font-size:0.75rem; color:var(--muted-color); margin-bottom:0.45rem; font-family:var(--nav-font); letter-spacing:0.05em;">UPI ID</span>
          <input type="text" class="checkout-input" id="payment-upi-id" placeholder="yourname@upi (e.g. 9876543210@ybl)" />
          <div class="field-error" id="payment-upi-err">Please enter a valid UPI ID</div>
        </label>
      </div>

      <!-- Card Fields (shown for card) -->
      <div class="payment-card-fields" id="payment-card-fields">
        <div class="checkout-field" style="margin-bottom:0;">
          <label style="display:block; font-size:0.75rem; color:var(--muted-color); margin-bottom:0.45rem; font-family:var(--nav-font);">Card Number</label>
          <input type="text" class="checkout-input" id="payment-card-num" placeholder="1234 5678 9012 3456" maxlength="19" />
          <div class="field-error" id="payment-card-err">Please enter a valid 16-digit card number</div>
        </div>
        <div class="payment-card-row">
          <div class="checkout-field" style="margin-bottom:0;">
            <label style="display:block; font-size:0.75rem; color:var(--muted-color); margin-bottom:0.45rem; font-family:var(--nav-font);">Expiry (MM/YY)</label>
            <input type="text" class="checkout-input" id="payment-card-expiry" placeholder="MM/YY" maxlength="5" />
          </div>
          <div class="checkout-field" style="margin-bottom:0;">
            <label style="display:block; font-size:0.75rem; color:var(--muted-color); margin-bottom:0.45rem; font-family:var(--nav-font);">CVV</label>
            <input type="password" class="checkout-input" id="payment-card-cvv" placeholder="&bull;&bull;&bull;" maxlength="4" />
          </div>
        </div>
        <div class="checkout-field" style="margin-bottom:0;">
          <label style="display:block; font-size:0.75rem; color:var(--muted-color); margin-bottom:0.45rem; font-family:var(--nav-font);">Cardholder Name</label>
          <input type="text" class="checkout-input" id="payment-card-name" placeholder="Name on card" autocomplete="cc-name" />
        </div>
      </div>

      <button class="pay-now-btn" id="pay-now-btn" onclick="submitPayment()">
        PAY NOW &rarr;
      </button>

      <p class="payment-secure-notice">
        <span>&#128274; 256-Bit Encrypted</span>
        <span>&#10003; PCI DSS Compliant</span>
        <span>&#9989; Instant Confirmation</span>
      </p>
    </div>
  </div>

  <!-- =====================================================
       ORDER SUCCESS MODAL
       ===================================================== -->
  <div class="order-success-backdrop" id="order-success-modal" role="dialog" aria-modal="true" aria-label="Order Confirmed">
    <div class="order-success-card">
      <div class="success-checkmark">&#10003;</div>
      <h2 class="success-title">Order Confirmed!</h2>
      <p class="success-subtitle">
        Thank you for choosing ÉLIXORA.<br>
        Your exquisite fragrance is being prepared for express air dispatch.<br>
        You'll receive a confirmation SMS and email shortly.
      </p>
      <div class="success-order-id">
        <div class="label">Order ID</div>
        <div class="id" id="success-order-id-display">ELX-000000</div>
      </div>
      <div style="font-size: 0.78rem; color: var(--muted-color); margin-bottom: 1.8rem; line-height: 1.7;">
        📦 Expected delivery: <strong style="color:#fff;">3–5 business days</strong><br>
        🚀 Express Air Delivery — Free of Charge<br>
        📧 Tracking ID dispatched to your email &amp; mobile
      </div>
      <button class="success-close-btn" onclick="closeOrderSuccessModal()">
        CONTINUE SHOPPING
      </button>
    </div>
  </div>

  <!-- ==========================================================
       ADMIN LOGIN MODAL
       ========================================================== -->
  <div class="admin-login-modal-backdrop" id="admin-login-modal" onclick="closeAdminLoginOnBackdrop(event)">
    <div class="admin-login-card">
      <button class="modal-close-btn" onclick="closeAdminLoginModal()">&times;</button>
      <div style="margin-bottom: 1rem;">
        <span class="section-eyebrow">ÉLIXORA ATELIER</span>
        <h3 style="font-family: var(--heading-font); font-size: 1.4rem; color: #fff; margin: 6px 0;">
          Staff / Admin Portal
        </h3>
        <p style="font-size: 0.8rem; color: var(--muted-color);">
          Enter Master Security PIN to manage live orders & store operations.
        </p>
      </div>

      <form onsubmit="handleAdminLogin(event)">
        <input type="password" id="admin-pin-input" class="admin-pin-input" maxlength="8" placeholder="••••" autocomplete="current-password" autofocus />
        <div id="admin-login-err" style="color: #ef4444; font-size: 0.78rem; margin-bottom: 12px; display: none;">
          Incorrect PIN. Enter Master Security PIN.
        </div>
        <button type="submit" class="primary-btn" style="width: 100%; justify-content: center;">
          UNLOCK ATELIER PORTAL &rarr;
        </button>
        <p style="font-size: 0.72rem; color: rgba(255,255,255,0.4); margin-top: 10px;">
          Confidential Master Access PIN
        </p>
      </form>
    </div>
  </div>

  <!-- ==========================================================
       FULL-SCREEN ADMIN DASHBOARD & LIVE ORDER MANAGEMENT
       ========================================================== -->
  <div class="admin-portal-view" id="admin-portal">
    <!-- Admin Top Header -->
    <header class="admin-top-bar">
      <div class="admin-brand-wrap">
        <span class="admin-brand-tag">ÉLIXORA</span>
        <span class="admin-badge-atelier">ATELIER OPERATING SYSTEM</span>
      </div>
      <div class="admin-actions-wrap">
        <button class="secondary-btn" onclick="closeAdminPortal()" style="padding: 8px 16px; font-size: 0.78rem;">
          &larr; Return to Storefront
        </button>
        <button class="icon-button" onclick="handleAdminLogout()" title="Lock / Logout" style="border-color: rgba(239, 68, 68, 0.4); color: #f87171;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
            <polyline points="16 17 21 12 16 7"></polyline>
            <line x1="21" y1="12" x2="9" y2="12"></line>
          </svg>
        </button>
      </div>
    </header>

    <div class="admin-portal-content">
      <!-- Top Stats Overview -->
      <div class="admin-stats-grid">
        <div class="admin-stat-card">
          <span class="admin-stat-label">Total Orders</span>
          <span class="admin-stat-val" id="admin-stat-total-orders">0</span>
          <span class="admin-stat-sub">Across All Channels</span>
        </div>
        <div class="admin-stat-card">
          <span class="admin-stat-label">Total Revenue</span>
          <span class="admin-stat-val" id="admin-stat-total-rev">₹0</span>
          <span class="admin-stat-sub">Gross Perfume Volume</span>
        </div>
        <div class="admin-stat-card">
          <span class="admin-stat-label">Pending / Placed</span>
          <span class="admin-stat-val" id="admin-stat-pending-orders" style="color: var(--gold-light);">0</span>
          <span class="admin-stat-sub">Awaiting Dispatch</span>
        </div>
        <div class="admin-stat-card">
          <span class="admin-stat-label">Dispatched / Shipped</span>
          <span class="admin-stat-val" id="admin-stat-shipped-orders" style="color: #c084fc;">0</span>
          <span class="admin-stat-sub">In BlueDart Air Transit</span>
        </div>
        <div class="admin-stat-card">
          <span class="admin-stat-label">Completed Delivery</span>
          <span class="admin-stat-val" id="admin-stat-delivered-orders" style="color: #4ade80;">0</span>
          <span class="admin-stat-sub">Fulfilled with Honors</span>
        </div>
      </div>

      <!-- Orders Filter Toolbar -->
      <div class="admin-toolbar">
        <div class="admin-filter-tabs">
          <button class="admin-filter-btn active" onclick="filterAdminOrders('all', this)">All Orders (<span id="count-all">0</span>)</button>
          <button class="admin-filter-btn" onclick="filterAdminOrders('Placed', this)">Placed (<span id="count-placed">0</span>)</button>
          <button class="admin-filter-btn" onclick="filterAdminOrders('Processing', this)">Processing (<span id="count-processing">0</span>)</button>
          <button class="admin-filter-btn" onclick="filterAdminOrders('Shipped', this)">Shipped (<span id="count-shipped">0</span>)</button>
          <button class="admin-filter-btn" onclick="filterAdminOrders('Delivered', this)">Delivered (<span id="count-delivered">0</span>)</button>
          <button class="admin-filter-btn" onclick="filterAdminOrders('Cancelled', this)">Cancelled (<span id="count-cancelled">0</span>)</button>
        </div>

        <div class="admin-search-wrap">
          <input type="text" class="custom-text-input" id="admin-order-search" placeholder="Search Order ID, Customer, Phone..." oninput="handleAdminOrderSearch(this.value)" style="padding: 7px 14px; font-size: 0.78rem; width: 100%;" />
        </div>
      </div>

      <!-- Live Orders Table -->
      <div class="admin-orders-table-wrap">
        <div style="overflow-x: auto;">
          <table class="admin-table">
            <thead>
              <tr>
                <th>Order ID & Date</th>
                <th>Customer Details</th>
                <th>Delivery Address</th>
                <th>Items Ordered</th>
                <th>Total & Payment</th>
                <th>Live Status & Action</th>
              </tr>
            </thead>
            <tbody id="admin-orders-tbody">
              <!-- Dynamically populated -->
            </tbody>
          </table>
        </div>
        <div id="admin-empty-state" style="padding: 3rem; text-align: center; color: var(--muted-color); display: none;">
          <p style="font-size: 0.9rem;">No customer orders found matching this filter.</p>
        </div>
      </div>
    </div>
  </div>

"""
