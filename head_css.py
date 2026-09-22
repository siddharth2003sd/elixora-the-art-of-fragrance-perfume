HEAD_AND_CSS = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ÉLIXORA — The Art of Fragrance | Haute Parfumerie</title>
  <meta name="description" content="ÉLIXORA is a luxury digital fragrance destination where every scent tells a story. Discover bespoke perfumes, notes, and cinematic 3D flacons.">
  <meta property="og:title" content="ÉLIXORA — The Art of Fragrance">
  <meta property="og:description" content="Where every scent tells a story. Explore haute parfumerie, 3D flacons, and personalized scent discovery.">
  <meta property="og:type" content="website">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Manrope:wght@400;500;600;700&family=Outfit:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&display=swap" rel="stylesheet">

  <!-- GSAP & Model Viewer CDN -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  <script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>

  <style>
    :root {
      --bg-color: #070707;
      --text-color: #ffffff;
      --cream: #f8f2e8;
      --gold: #d4af70;
      --gold-light: #ead7a6;
      --accent: #fbcfe8;
      --burgundy: #3a0d1f;
      --wine: #64152d;
      --emerald: #073b35;
      --muted-color: rgba(255, 255, 255, 0.68);
      --glass-bg: rgba(255, 255, 255, 0.055);
      --glass-border: rgba(255, 255, 255, 0.12);
      --heading-font: 'Playfair Display', serif;
      --body-font: 'Inter', sans-serif;
      --nav-font: 'Manrope', sans-serif;
      --trans-smooth: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    html {
      scroll-behavior: smooth;
      overscroll-behavior-x: none;
      overscroll-behavior-y: auto;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }

    body {
      overflow-x: hidden;
      min-height: 100vh;
      background-color: var(--bg-color);
      color: var(--text-color);
      font-family: var(--body-font);
      font-size: 16px;
      line-height: 1.6;
      position: relative;
      overscroll-behavior-x: none;
      overscroll-behavior-y: auto;
      -webkit-overflow-scrolling: touch;
    }

    /* Custom Luxury Scrollbar */
    ::-webkit-scrollbar {
      width: 6px;
    }
    ::-webkit-scrollbar-track {
      background: #080808;
    }
    ::-webkit-scrollbar-thumb {
      background: rgba(212, 175, 112, 0.3);
      border-radius: 3px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: var(--gold);
    }

    /* Dynamic Canvas / Radial Background */
    #bg-layer {
      display: none;
    }

    #particles-canvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: -1;
      pointer-events: none;
    }

    /* Custom Luxury Cursor */
    .custom-cursor {
      position: fixed;
      top: 0;
      left: 0;
      width: 10px;
      height: 10px;
      background: #fff;
      border-radius: 50%;
      pointer-events: none;
      z-index: 9999;
      transform: translate(-50%, -50%);
      transition: width 0.25s ease, height 0.25s ease, background 0.25s ease, border-color 0.25s ease;
    }
    .custom-cursor-follower {
      position: fixed;
      top: 0;
      left: 0;
      width: 36px;
      height: 36px;
      border: 1px solid rgba(212, 175, 112, 0.5);
      border-radius: 50%;
      pointer-events: none;
      z-index: 9998;
      transform: translate(-50%, -50%);
      transition: transform 0.12s ease-out, width 0.3s ease, height 0.3s ease, border-color 0.3s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 9px;
      letter-spacing: 1.5px;
      font-family: var(--nav-font);
      color: transparent;
      text-transform: uppercase;
    }
    .custom-cursor-follower.hovering {
      width: 56px;
      height: 56px;
      border-color: var(--gold);
      background: rgba(212, 175, 112, 0.08);
      backdrop-filter: blur(2px);
    }
    .custom-cursor-follower.view-mode {
      width: 68px;
      height: 68px;
      border-color: var(--accent);
      background: rgba(251, 207, 232, 0.15);
      color: #fff;
      font-weight: 600;
    }

    /* Typography */
    h1, h2, h3, h4, .serif-font {
      font-family: var(--heading-font);
      font-weight: 400;
      letter-spacing: -0.02em;
    }
    .nav-font {
      font-family: var(--nav-font);
    }

    /* Luxury Header */
    .header {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 64px;
      padding: 0 clamp(1.5rem, 3.5vw, 3.5rem);
      display: flex;
      align-items: center;
      justify-content: space-between;
      z-index: 100;
      transition: height 0.3s ease, background 0.3s ease, border-color 0.3s ease, backdrop-filter 0.3s ease;
    }
    .header.scrolled {
      height: 54px;
      background: rgba(7, 7, 7, 0.85);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid var(--glass-border);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }
    .brand-logo {
      display: flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
      text-decoration: none;
      color: #fff;
    }
    .logo-symbol {
      width: 30px;
      height: 30px;
      border: 1px solid var(--gold);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      background: radial-gradient(circle, rgba(212, 175, 112, 0.25) 0%, transparent 70%);
      transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.6s ease;
    }
    .logo-symbol::before {
      content: "";
      position: absolute;
      width: 14px;
      height: 14px;
      border: 1px solid var(--gold-light);
      transform: rotate(45deg);
    }
    .logo-symbol::after {
      content: "";
      width: 4px;
      height: 4px;
      background: var(--gold);
      border-radius: 50%;
      box-shadow: 0 0 10px var(--gold);
    }
    .brand-logo:hover .logo-symbol {
      transform: rotate(180deg) scale(1.05);
      box-shadow: 0 0 20px rgba(212, 175, 112, 0.4);
    }
    .brand-name {
      font-family: var(--heading-font);
      font-size: 1.25rem;
      letter-spacing: 0.22em;
      font-weight: 500;
      background: linear-gradient(135deg, #ffffff 40%, var(--gold-light) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    /* Navigation Bar */
    .nav.glass {
      display: flex;
      align-items: center;
      gap: clamp(0.35rem, 0.75vw, 0.95rem);
      padding: 0.32rem clamp(0.65rem, 1vw, 1.15rem);
      border-radius: 100px;
      background: var(--glass-bg);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--glass-border);
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
      white-space: nowrap;
    }
    .nav-item {
      color: var(--muted-color);
      text-decoration: none;
      font-family: var(--nav-font);
      font-size: 0.76rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      font-weight: 500;
      position: relative;
      padding: 4px 6px;
      white-space: nowrap;
      transition: color 0.3s ease, font-size 0.3s ease;
      cursor: pointer;
    }
    .nav-item::after {
      content: "";
      position: absolute;
      bottom: 0;
      left: 50%;
      width: 0%;
      height: 1px;
      background: var(--gold);
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      transform: translateX(-50%);
    }
    .nav-item:hover, .nav-item.active {
      color: #ffffff;
    }
    .nav-item:hover::after, .nav-item.active::after {
      width: 100%;
    }

    /* Header Actions */
    .header-actions {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }
    .icon-button {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: var(--glass-bg);
      border: 1px solid var(--glass-border);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      transition: var(--trans-smooth);
      position: relative;
    }
    .icon-button:hover {
      background: rgba(255, 255, 255, 0.12);
      border-color: var(--gold);
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
    }
    .badge-count {
      position: absolute;
      top: -3px;
      right: -3px;
      background: var(--accent);
      color: #1b0a12;
      font-size: 10px;
      font-weight: 700;
      width: 17px;
      height: 17px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
    }
    .cart-button {
      padding: 0 1rem;
      height: 36px;
      border-radius: 100px;
      background: var(--glass-bg);
      border: 1px solid var(--glass-border);
      color: #fff;
      font-family: var(--nav-font);
      font-size: 0.76rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      transition: var(--trans-smooth);
    }
    .cart-button:hover {
      border-color: var(--gold);
      background: rgba(212, 175, 112, 0.15);
      transform: translateY(-2px);
      box-shadow: 0 8px 25px rgba(212, 175, 112, 0.2);
    }
    .cart-button span {
      background: var(--gold);
      color: #070707;
      font-weight: 700;
      font-size: 11px;
      padding: 1px 6px;
      border-radius: 10px;
    }

    .hamburger-btn {
      display: none;
      width: 42px;
      height: 42px;
      border-radius: 50%;
      background: var(--glass-bg);
      border: 1px solid var(--glass-border);
      color: #fff;
      cursor: pointer;
      align-items: center;
      justify-content: center;
    }

    /* Hero Campaign Section (100% Full-Screen Edge-to-Edge Luxury Advertising Campaign - Fully Covered) */
    .hero-section {
      min-height: 100vh;
      height: 100vh;
      min-height: 100dvh;
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: flex-start;
      padding: 0;
      position: relative;
      overflow: hidden;
      background: #060403;
    }

    /* Ambient base layers */
    .bg-layer-base, .bg-layer-transition {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: -3;
      pointer-events: none;
      transition: opacity 1s cubic-bezier(0.25, 1, 0.5, 1);
    }
    .bg-layer-base {
      background: radial-gradient(circle at 50% 50%, #120A03 0%, #080402 70%, #000000 100%);
    }

    .luxury-grain-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 3;
      pointer-events: none;
      opacity: 0.04;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
    }

    /* 100% Edge-to-Edge Photograph Canvas Stage */
    .hero-backdrop-stage {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      z-index: 1;
      overflow: hidden;
      pointer-events: none;
    }

    /* Full-Screen Hero Image spanning edge to edge with object-fit: cover (Fully Covered, No Circle) */
    .hero-campaign-full-img {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: 70% center;
      pointer-events: none;
      z-index: 1;
      will-change: opacity, transform;
      transition: opacity 0.5s cubic-bezier(0.25, 1, 0.5, 1);
    }
    .hero-campaign-full-img-next {
      opacity: 0;
      z-index: 2;
    }

    /* Soft luxury atmospheric scrim allowing the full photograph to shine through edge to edge */
    .hero-campaign-scrim {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      z-index: 2;
      pointer-events: none;
      background: 
        /* Delicate left-to-right gradient: softens brightness behind text while keeping rich photographic scene fully visible */
        linear-gradient(90deg, 
          rgba(6, 4, 3, 0.65) 0%, 
          rgba(6, 4, 3, 0.48) 32%, 
          rgba(6, 4, 3, 0.15) 55%, 
          transparent 75%
        ),
        /* Top and bottom atmospheric shading for header and aura switcher bar */
        linear-gradient(180deg, 
          rgba(6, 4, 3, 0.55) 0%, 
          transparent 16%, 
          transparent 82%, 
          rgba(6, 4, 3, 0.65) 100%
        );
    }

    /* Product Text Overlay: Situated in the darker/negative space on the left */
    .hero-left {
      position: relative;
      z-index: 10;
      max-width: 640px;
      padding-left: clamp(2.5rem, 7vw, 7.5rem);
      padding-right: 2rem;
      padding-top: 1.5rem;
    }
    .eyebrow {
      font-family: var(--nav-font);
      font-size: 0.85rem;
      letter-spacing: 0.3em;
      text-transform: uppercase;
      color: var(--gold);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 12px;
      font-weight: 600;
    }
    .eyebrow::before {
      content: "";
      width: 24px;
      height: 1px;
      background: var(--gold);
    }
    .hero-heading {
      font-size: clamp(2.8rem, 5.2vw, 5.2rem);
      line-height: 1.12;
      margin-bottom: 1.5rem;
      color: #fff;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      font-family: var(--heading-font);
      text-shadow: 0 4px 30px rgba(0, 0, 0, 0.75);
    }
    .hero-category-badge-wrap {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 2rem;
      flex-wrap: wrap;
    }
    .hero-category-badge {
      font-family: var(--nav-font);
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.18em;
      color: var(--gold-light);
      background: rgba(212, 175, 112, 0.15);
      border: 1px solid rgba(212, 175, 112, 0.3);
      padding: 5px 14px;
      border-radius: 4px;
      text-transform: uppercase;
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
    }
    .hero-mood-badge {
      font-family: var(--body-font);
      font-size: 0.78rem;
      font-weight: 400;
      letter-spacing: 0.06em;
      color: rgba(255, 255, 255, 0.75);
      text-transform: lowercase;
      font-style: italic;
      text-shadow: 0 1px 8px rgba(0, 0, 0, 0.7);
    }
    .hero-tagline {
      font-size: 1.15rem;
      color: rgba(255, 255, 255, 0.92);
      max-width: 520px;
      margin-bottom: 2.75rem;
      font-weight: 300;
      line-height: 1.85;
      text-shadow: 0 2px 16px rgba(0, 0, 0, 0.85);
    }
    .hero-actions {
      display: flex;
      align-items: center;
      gap: 1.5rem;
    }

    /* Minimalist luxury control bar at bottom center of the hero section */
    
    /* Hide legacy pill bar */
    .theme-morph-bar {
      display: none !important;
    }

    /* Luxury Left & Right Edge Navigation Arrows */
    .hero-edge-nav-btn {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      z-index: 50;
      width: 52px;
      height: 52px;
      border-radius: 50%;
      background: rgba(10, 10, 10, 0.45);
      border: 1px solid rgba(212, 175, 112, 0.35);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .hero-edge-nav-btn:hover {
      background: rgba(212, 175, 112, 0.25);
      border-color: var(--gold);
      color: var(--gold-light);
      transform: translateY(-50%) scale(1.1);
      box-shadow: 0 12px 35px rgba(212, 175, 112, 0.35);
    }
    .hero-edge-nav-btn:active {
      transform: translateY(-50%) scale(0.95);
    }
    .hero-edge-prev {
      left: 2rem;
    }
    .hero-edge-next {
      right: 2rem;
    }

    @media (max-width: 900px) {
      .hero-edge-nav-btn {
        width: 44px;
        height: 44px;
        top: 45%;
      }
      .hero-edge-prev {
        left: 0.75rem;
      }
      .hero-edge-next {
        right: 0.75rem;
      }
    }

    .hero-carousel-controls-bar {
      position: absolute;
      bottom: 6.5rem;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      align-items: center;
      gap: 1.5rem;
      z-index: 20;
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 10px 24px;
      border-radius: 100px;
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
    }
    .hero-carousel-arrow {
      background: none;
      border: none;
      color: rgba(255, 255, 255, 0.65);
      cursor: pointer;
      width: 32px;
      height: 32px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      transition: var(--trans-smooth);
    }
    .hero-carousel-arrow:hover {
      color: #fff;
      background: rgba(255, 255, 255, 0.1);
    }
    .hero-carousel-dots {
      display: flex;
      align-items: center;
      gap: 8px;
      max-width: 300px;
      overflow-x: auto;
      scrollbar-width: none;
    }
    .hero-carousel-dots::-webkit-scrollbar {
      display: none;
    }
    .hero-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.2);
      border: none;
      cursor: pointer;
      transition: all 0.3s ease;
      padding: 0;
      margin: 0 4px;
    }
    .hero-dot.active {
      background: var(--gold);
      box-shadow: 0 0 8px rgba(212, 175, 112, 0.6);
      transform: scale(1.2);
    }
    .card-badge {
      font-size: 0.8rem;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      font-family: var(--nav-font);
      font-weight: 600;
      color: var(--gold);
      margin-bottom: 0.75rem;
      display: block;
    }
    .card-title {
      font-size: 1.5rem;
      margin-bottom: 0.35rem;
      color: #fff;
    }
    .card-subtitle {
      font-size: 0.92rem;
      color: var(--muted-color);
      margin-bottom: 1rem;
    }
    .card-preview-thumb {
      width: 100%;
      height: 160px;
      border-radius: 12px;
      overflow: hidden;
      margin-bottom: 1.25rem;
      background: radial-gradient(circle, rgba(212, 175, 112, 0.1) 0%, rgba(0, 0, 0, 0.4) 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: transform 0.5s ease;
    }
    .card-preview-thumb img {
      height: 90%;
      object-fit: contain;
    }
    .card-rating {
      color: var(--gold);
      font-size: 0.85rem;
      margin-bottom: 0.5rem;
      letter-spacing: 2px;
    }
    .card-footer-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: 0.75rem;
      padding-top: 0.75rem;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
    }
    .card-price {
      font-size: 1.35rem;
      font-weight: 600;
      color: #fff;
      font-family: var(--nav-font);
    }
    .card-link {
      font-size: 0.88rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--gold);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 6px;
      font-family: var(--nav-font);
      font-weight: 600;
      transition: gap 0.3s ease;
    }
    .featured-glass-card:hover .card-link {
      gap: 10px;
    }

    /* Hero Signature Perfume Carousel Styling */
    .hero-carousel-wrapper {
      width: 100%;
      max-width: 330px;
      padding: 1.5rem 1.4rem;
      border-radius: 20px;
      background: rgba(255, 255, 255, 0.04);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid var(--glass-border);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
      position: relative;
      overflow: hidden;
      transition: border-color 0.4s ease, box-shadow 0.4s ease;
    }
    .hero-carousel-wrapper::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 1px;
      background: linear-gradient(90deg, transparent, var(--gold-light), transparent);
      opacity: 0.6;
      z-index: 2;
    }
    .hero-carousel-wrapper:hover {
      border-color: rgba(212, 175, 112, 0.45);
      box-shadow: 0 25px 60px rgba(212, 175, 112, 0.12), 0 10px 30px rgba(0, 0, 0, 0.6);
    }
    .hero-carousel-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 0.85rem;
    }
    .hero-carousel-header .card-badge {
      margin-bottom: 0;
      font-size: 0.72rem;
    }
    .hero-carousel-timer-pill {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 3px 9px;
      border-radius: 100px;
      background: rgba(212, 175, 112, 0.1);
      border: 1px solid rgba(212, 175, 112, 0.25);
      font-family: var(--nav-font);
      font-size: 0.65rem;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--gold-light);
    }
    .hero-carousel-viewport {
      width: 100%;
      overflow: hidden;
      position: relative;
      cursor: grab;
      user-select: none;
      -webkit-user-select: none;
      touch-action: pan-y;
      border-radius: 14px;
    }
    .hero-carousel-viewport:active {
      cursor: grabbing;
    }
    .hero-carousel-track {
      display: flex;
      width: 100%;
      will-change: transform;
      transition: transform 0.65s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .hero-carousel-slide {
      flex: 0 0 100%;
      width: 100%;
      box-sizing: border-box;
      padding: 0.75rem 0.25rem 0.5rem 0.25rem;
      cursor: pointer;
    }
    .hero-slide-badge {
      font-size: 0.68rem;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      font-family: var(--nav-font);
      color: var(--gold);
      margin-bottom: 0.35rem;
    }
    .hero-carousel-slide .card-title {
      font-size: 1.4rem;
      margin-bottom: 0.2rem;
      letter-spacing: 0.04em;
    }
    .hero-carousel-slide .card-subtitle {
      font-size: 0.8rem;
      color: var(--muted-color);
      margin-bottom: 0.85rem;
      line-height: 1.4;
    }
    .hero-carousel-slide .card-preview-thumb {
      height: 175px;
      border-radius: 12px;
      overflow: hidden;
      margin-bottom: 0.85rem;
      background: rgba(0, 0, 0, 0.3);
      border: 1px solid rgba(255, 255, 255, 0.05);
      transition: transform 0.4s ease;
    }
    .hero-carousel-slide:hover .card-preview-thumb {
      transform: scale(1.04);
    }
    .hero-carousel-slide .card-preview-thumb img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s ease;
    }
    .hero-carousel-slide .card-rating {
      color: var(--gold);
      font-size: 0.85rem;
      letter-spacing: 2px;
      margin-bottom: 0.5rem;
    }
    .hero-carousel-slide .card-footer-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      padding-top: 0.65rem;
    }
    .hero-carousel-slide .card-price {
      font-family: var(--display-font);
      font-size: 1.15rem;
      color: #fff;
    }

    /* Carousel Controls: Arrows + Indicator Buttons */
    .hero-carousel-controls {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: 0.75rem;
      padding-top: 0.75rem;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
    }
    .hero-carousel-arrow {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: var(--muted-color);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.3s ease;
    }
    .hero-carousel-arrow:hover {
      background: var(--gold);
      border-color: var(--gold);
      color: #0d121c;
      transform: scale(1.08);
    }
    .hero-carousel-dots {
      display: flex;
      align-items: center;
      gap: 4px;
      flex-wrap: nowrap;
      max-width: 280px;
      overflow-x: auto;
      scrollbar-width: none;
    }
    .hero-carousel-dots::-webkit-scrollbar {
      display: none;
    }
    .hero-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.2);
      border: none;
      cursor: pointer;
      transition: all 0.3s ease;
      padding: 0;
      margin: 0 4px;
    }
    .hero-dot:hover, .hero-dot.active {
      background: var(--gold);
      box-shadow: 0 0 8px rgba(212, 175, 112, 0.6);
      transform: scale(1.2);
    }

    /* Scent Theme Morph Switcher Bar */
    .theme-morph-bar {
      position: absolute;
      bottom: 1.5rem;
      left: 4rem;
      display: flex;
      align-items: center;
      gap: 1.25rem;
      z-index: 20;
      max-width: calc(100vw - 8rem);
    }
    .theme-morph-label {
      font-size: 0.82rem;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      font-family: var(--nav-font);
      color: var(--muted-color);
      flex-shrink: 0;
    }
    .theme-pills {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      scroll-behavior: smooth;
      padding: 4px 0;
      scrollbar-width: none; /* Firefox */
      -ms-overflow-style: none; /* IE 10+ */
    }
    .theme-pills::-webkit-scrollbar {
      display: none; /* Chrome, Safari, Opera */
    }
    .theme-pill-btn {
      flex-shrink: 0;
      padding: 7px 16px;
      border-radius: 100px;
      background: var(--glass-bg);
      border: 1px solid var(--glass-border);
      color: var(--muted-color);
      font-family: var(--nav-font);
      font-size: 0.82rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      cursor: pointer;
      backdrop-filter: blur(10px);
      transition: var(--trans-smooth);
    }
    .theme-pill-btn:hover, .theme-pill-btn.active {
      color: #fff;
      border-color: var(--gold);
      background: rgba(212, 175, 112, 0.15);
    }

    /* Sections Common */
    .section-container {
      padding: 7rem 4rem;
      position: relative;
    }
    .section-header {
      margin-bottom: 4rem;
    }
    .section-header.centered {
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .section-eyebrow {
      font-family: var(--nav-font);
      font-size: 0.82rem;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--gold);
      margin-bottom: 1rem;
      display: block;
    }
    .section-title {
      font-size: clamp(2.1rem, 4vw, 3.4rem);
      line-height: 1.15;
      color: #fff;
      margin-bottom: 1rem;
    }
    .section-subtitle {
      font-size: 1.05rem;
      line-height: 1.65;
      color: var(--muted-color);
      max-width: 620px;
      font-weight: 300;
    }

    /* Fragrance Collections Grid (6 Moods) */
    .collections-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 2rem;
    }
    .collection-card {
      position: relative;
      height: 500px;
      border-radius: 20px;
      overflow: hidden;
      border: 1px solid var(--glass-border);
      cursor: pointer;
      background: #0d0d0d;
      will-change: transform, box-shadow, border-color;
    }
    .collection-bg-img {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      filter: brightness(0.62) saturate(0.95);
      will-change: transform, filter;
      transform-origin: center center;
    }
    .collection-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(7, 7, 7, 0.15) 0%, rgba(7, 7, 7, 0.45) 45%, rgba(7, 7, 7, 0.94) 90%);
      will-change: opacity;
    }
    .collection-content {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      padding: 2.25rem 2.25rem 2rem 2.25rem;
      z-index: 2;
      will-change: transform;
    }
    .collection-family {
      font-size: 0.82rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      font-family: var(--nav-font);
      color: var(--gold);
      margin-bottom: 0.4rem;
      display: block;
    }
    .collection-name {
      font-size: 2.2rem;
      line-height: 1.1;
      margin-bottom: 0.5rem;
      color: #fff;
      font-family: var(--heading-font);
      letter-spacing: 0.02em;
    }
    .collection-desc {
      font-size: 0.86rem;
      color: var(--muted-color);
      line-height: 1.55;
      margin-bottom: 0.9rem;
      max-width: 95%;
      font-weight: 300;
    }
    .collection-notes-list {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 0.75rem;
    }
    .collection-note-pill {
      font-size: 0.8rem;
      padding: 3px 10px;
      border-radius: 100px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(8px);
      color: var(--cream);
      font-family: var(--nav-font);
      transition: background 0.3s ease, border-color 0.3s ease;
    }
    .collection-extra-details {
      overflow: hidden;
      height: 0;
      opacity: 0;
      will-change: height, opacity;
    }
    .collection-meta-row {
      display: flex;
      flex-direction: column;
      gap: 4px;
      margin: 0.6rem 0 1rem 0;
      padding-top: 0.75rem;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
    }
    .collection-meta-item {
      font-size: 0.8rem;
      color: var(--muted-color);
      font-family: var(--nav-font);
      letter-spacing: 0.04em;
    }
    .collection-meta-item em {
      color: var(--gold-light);
      font-style: normal;
      font-weight: 600;
      margin-right: 4px;
    }
    .collection-explore-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 0.88rem;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      font-family: var(--nav-font);
      color: var(--gold);
      font-weight: 600;
      transition: gap 0.3s ease, color 0.3s ease;
      margin-top: 0.25rem;
    }
    .collection-card:hover .collection-explore-btn {
      gap: 14px;
      color: #fff;
    }

    /* Catalog Section & Filter Bar */
    .catalog-controls {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      margin-bottom: 3.5rem;
    }
    .catalog-filter-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1.25rem;
    }
    .filter-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }
    .filter-btn {
      padding: 8px 20px;
      border-radius: 100px;
      background: var(--glass-bg);
      border: 1px solid var(--glass-border);
      color: var(--muted-color);
      font-family: var(--nav-font);
      font-size: 0.88rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      cursor: pointer;
      backdrop-filter: blur(12px);
      transition: var(--trans-smooth);
    }
    .filter-btn:hover, .filter-btn.active {
      color: #070707;
      background: var(--cream);
      border-color: var(--cream);
      font-weight: 600;
      box-shadow: 0 4px 15px rgba(248, 242, 232, 0.2);
    }
    .catalog-sort-group {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .sort-label {
      font-size: 0.85rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--muted-color);
      font-family: var(--nav-font);
    }
    .custom-select {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--glass-border);
      color: #fff;
      font-family: var(--nav-font);
      font-size: 0.85rem;
      padding: 8px 16px;
      border-radius: 100px;
      outline: none;
      cursor: pointer;
      backdrop-filter: blur(12px);
    }
    .custom-select option {
      background: #121212;
      color: #fff;
    }

    /* Product Cards Carousel & Slider System */
    .products-carousel-wrapper {
      position: relative;
      width: 100%;
      margin-top: 1rem;
      padding: 0.5rem 0;
    }
    .carousel-viewport {
      width: 100%;
      overflow: hidden;
      position: relative;
      border-radius: 24px;
      padding: 10px 0;
    }
    .products-grid {
      display: flex;
      flex-direction: row;
      flex-wrap: nowrap;
      gap: 2rem;
      will-change: transform;
      user-select: none;
    }
    .product-card {
      flex: 0 0 calc((100% - 6rem) / 4);
      min-width: 280px;
      box-sizing: border-box;
      background: rgba(255, 255, 255, 0.035);
      border: 1px solid var(--glass-border);
      border-radius: 20px;
      overflow: hidden;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      position: relative;
      transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.5s ease, border-color 0.5s ease;
      cursor: pointer;
    }
    @media (max-width: 1200px) {
      .product-card {
        flex: 0 0 calc((100% - 4rem) / 3);
      }
    }
    @media (max-width: 860px) {
      .product-card {
        flex: 0 0 calc((100% - 2rem) / 2);
      }
    }
    @media (max-width: 560px) {
      .product-card {
        flex: 0 0 88%;
      }
    }

    /* Carousel Nav Arrows & Indicator Bar */
    .carousel-arrow-btn {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: rgba(10, 10, 10, 0.85);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid var(--glass-border);
      color: var(--gold-light);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 10;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
    }
    .carousel-arrow-btn:hover {
      background: var(--gold);
      color: #0d0d0d;
      border-color: var(--gold);
      transform: translateY(-50%) scale(1.1);
      box-shadow: 0 10px 30px rgba(212, 175, 112, 0.4);
    }
    .carousel-arrow-btn.prev-btn {
      left: -24px;
    }
    .carousel-arrow-btn.next-btn {
      right: -24px;
    }
    @media (max-width: 768px) {
      .carousel-arrow-btn.prev-btn { left: 4px; }
      .carousel-arrow-btn.next-btn { right: 4px; }
    }

    .carousel-footer-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: 1.5rem;
      padding: 0 0.5rem;
    }
    .carousel-autoplay-status {
      display: flex;
      align-items: center;
      gap: 8px;
      font-family: var(--nav-font);
      font-size: 0.78rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--muted-color);
    }
    .autoplay-pulse-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--gold);
      box-shadow: 0 0 10px var(--gold);
      animation: autoPlayPulse 2s infinite ease-in-out;
    }
    @keyframes autoPlayPulse {
      0%, 100% { opacity: 0.4; transform: scale(0.9); }
      50% { opacity: 1; transform: scale(1.25); }
    }
    .carousel-dots-wrap {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .carousel-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.2);
      border: 1px solid transparent;
      transition: all 0.35s ease;
      cursor: pointer;
    }
    .carousel-dot.active {
      width: 28px;
      border-radius: 100px;
      background: var(--gold);
      box-shadow: 0 0 12px rgba(212, 175, 112, 0.5);
    }
    .product-card:hover {
      transform: translateY(-8px);
      border-color: rgba(212, 175, 112, 0.35);
      box-shadow: 0 20px 45px rgba(0, 0, 0, 0.6), 0 0 25px rgba(212, 175, 112, 0.1);
    }
    .card-top-actions {
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: absolute;
      top: 1.25rem;
      left: 1.25rem;
      right: 1.25rem;
      z-index: 5;
    }
    .tag-badge {
      font-size: 0.65rem;
      font-family: var(--nav-font);
      letter-spacing: 0.15em;
      text-transform: uppercase;
      padding: 3px 10px;
      border-radius: 100px;
      background: rgba(212, 175, 112, 0.2);
      border: 1px solid rgba(212, 175, 112, 0.4);
      color: var(--gold-light);
    }
    .tag-badge.bestseller {
      background: rgba(251, 207, 232, 0.2);
      border-color: rgba(251, 207, 232, 0.4);
      color: var(--accent);
    }
    .wishlist-toggle-btn {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: rgba(0, 0, 0, 0.4);
      backdrop-filter: blur(8px);
      border: 1px solid var(--glass-border);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.3s ease;
    }
    .wishlist-toggle-btn:hover, .wishlist-toggle-btn.active {
      color: #ff477e;
      border-color: #ff477e;
      background: rgba(255, 71, 126, 0.15);
      transform: scale(1.1);
    }

    .product-img-wrapper {
      width: 100%;
      height: 260px;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 1rem 0 1.5rem 0;
      border-radius: 14px;
      background: radial-gradient(circle, rgba(255, 255, 255, 0.04) 0%, transparent 70%);
      overflow: hidden;
    }
    .product-img-wrapper img {
      max-height: 88%;
      max-width: 88%;
      object-fit: contain;
      transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .product-card:hover .product-img-wrapper img {
      transform: scale(1.08) translateY(-4px);
    }
    .quick-view-overlay-btn {
      position: absolute;
      bottom: 12px;
      left: 50%;
      transform: translateX(-50%) translateY(20px);
      opacity: 0;
      background: rgba(7, 7, 7, 0.85);
      backdrop-filter: blur(12px);
      border: 1px solid var(--glass-border);
      color: #fff;
      font-family: var(--nav-font);
      font-size: 0.82rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      padding: 7px 20px;
      border-radius: 100px;
      cursor: pointer;
      transition: var(--trans-smooth);
      white-space: nowrap;
    }
    .product-card:hover .quick-view-overlay-btn {
      opacity: 1;
      transform: translateX(-50%) translateY(0);
    }
    .quick-view-overlay-btn:hover {
      border-color: var(--gold);
      color: var(--gold);
    }

    .product-info {
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }
    .product-brand {
      font-family: var(--nav-font);
      font-size: 0.82rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--gold);
      margin-bottom: 0.3rem;
    }
    .product-name {
      font-size: 1.38rem;
      color: #fff;
      margin-bottom: 0.35rem;
      line-height: 1.25;
    }
    .product-family-meta {
      font-size: 0.92rem;
      color: var(--muted-color);
      margin-bottom: 0.75rem;
    }
    .product-rating-stars {
      color: var(--gold);
      font-size: 0.9rem;
      letter-spacing: 2px;
      margin-bottom: 1rem;
    }
    .product-bottom-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: auto;
      padding-top: 1rem;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
    }
    .product-price-val {
      font-family: var(--nav-font);
      font-size: 1.3rem;
      font-weight: 600;
      color: #fff;
    }
    .add-to-bag-btn {
      padding: 8px 18px;
      border-radius: 100px;
      background: var(--glass-bg);
      border: 1px solid var(--glass-border);
      color: #fff;
      font-family: var(--nav-font);
      font-size: 0.86rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      cursor: pointer;
      backdrop-filter: blur(10px);
      transition: var(--trans-smooth);
    }
    .add-to-bag-btn:hover {
      background: var(--accent);
      color: #1b0a12;
      border-color: var(--accent);
      font-weight: 600;
    }

    /* Seasonal Tabs Section */
    .seasonal-tabs {
      display: flex;
      justify-content: center;
      gap: 12px;
      margin-bottom: 2rem;
      flex-wrap: wrap;
    }
    .seasonal-tab-btn {
      padding: 10px 28px;
      border-radius: 100px;
      background: var(--glass-bg);
      border: 1px solid var(--glass-border);
      color: var(--muted-color);
      font-family: var(--nav-font);
      font-size: 0.85rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      cursor: pointer;
      backdrop-filter: blur(12px);
      transition: var(--trans-smooth);
    }
    .seasonal-tab-btn:hover, .seasonal-tab-btn.active {
      background: var(--gold);
      color: #070707;
      border-color: var(--gold);
      font-weight: 600;
      box-shadow: 0 5px 20px rgba(212, 175, 112, 0.3);
    }

    .seasonal-banner-badge {
      display: inline-flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
      padding: 1.2rem 2rem;
      border-radius: 16px;
      background: rgba(212, 175, 112, 0.05);
      border: 1px solid rgba(212, 175, 112, 0.22);
      backdrop-filter: blur(12px);
      animation: fadeInSeasonal 0.4s ease-out;
    }
    @keyframes fadeInSeasonal {
      from { opacity: 0; transform: translateY(8px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .seasonal-badge-title {
      font-family: var(--heading-font);
      font-size: 1.15rem;
      letter-spacing: 0.12em;
      color: var(--gold);
      text-transform: uppercase;
      font-weight: 500;
    }
    .seasonal-badge-tagline {
      font-family: var(--nav-font);
      font-size: 0.78rem;
      letter-spacing: 0.14em;
      color: #fff;
      text-transform: uppercase;
    }
    .seasonal-badge-desc {
      font-size: 0.86rem;
      color: var(--muted-color);
      margin: 4px 0 0;
      line-height: 1.55;
      max-width: 680px;
    }

    /* Fragrance Moods Horizontal Carousel */
    .mood-cards-container {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 1.5rem;
    }
    .mood-card {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--glass-border);
      border-radius: 20px;
      padding: 2.5rem 1.75rem;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      cursor: pointer;
      transition: var(--trans-smooth);
      position: relative;
      overflow: hidden;
    }
    .mood-card::before {
      content: "";
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at center, rgba(212, 175, 112, 0.12) 0%, transparent 70%);
      opacity: 0;
      transition: opacity 0.5s ease;
    }
    .mood-card:hover {
      transform: translateY(-8px);
      border-color: var(--gold);
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
    }
    .mood-card:hover::before {
      opacity: 1;
    }
    .mood-icon {
      width: 52px;
      height: 52px;
      border-radius: 50%;
      border: 1px solid var(--glass-border);
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 1.5rem;
      color: var(--gold);
      background: rgba(255, 255, 255, 0.04);
      transition: transform 0.4s ease, border-color 0.4s ease;
    }
    .mood-card:hover .mood-icon {
      transform: scale(1.1) rotate(10deg);
      border-color: var(--gold);
    }
    .mood-feel {
      font-size: 0.72rem;
      letter-spacing: 0.25em;
      text-transform: uppercase;
      color: var(--muted-color);
      font-family: var(--nav-font);
      margin-bottom: 0.5rem;
    }
    .mood-name {
      font-size: 1.5rem;
      color: #fff;
      margin-bottom: 1rem;
    }
    .mood-arrow {
      color: var(--gold);
      font-size: 1.1rem;
      margin-bottom: 0.75rem;
    }
    .mood-scent-notes {
      font-size: 0.95rem;
      font-style: italic;
      color: var(--cream);
      font-family: var(--heading-font);
    }

    /* The Art of Ingredients */
    .ingredients-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.5rem;
    }
    .ingredient-card {
      background: rgba(255, 255, 255, 0.035);
      border: 1px solid var(--glass-border);
      border-radius: 20px;
      padding: 2.5rem 1.75rem;
      text-align: center;
      cursor: pointer;
      position: relative;
      overflow: hidden;
      transition: var(--trans-smooth);
    }
    .ingredient-card:hover {
      transform: translateY(-8px);
      border-color: var(--gold);
      box-shadow: 0 15px 40px rgba(0, 0, 0, 0.5);
    }
    .ingredient-origin {
      font-size: 0.7rem;
      letter-spacing: 0.25em;
      text-transform: uppercase;
      color: var(--gold);
      font-family: var(--nav-font);
      margin-bottom: 0.5rem;
      display: block;
    }
    .ingredient-name {
      font-size: 1.8rem;
      color: #fff;
      margin-bottom: 0.75rem;
    }
    .ingredient-desc {
      font-size: 0.85rem;
      color: var(--muted-color);
      line-height: 1.6;
    }

    /* Luxury Brands Section */
    .brands-banner {
      padding: 4rem 4rem;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      background: rgba(255, 255, 255, 0.015);
    }
    .brands-row {
      display: flex;
      align-items: center;
      justify-content: space-around;
      flex-wrap: wrap;
      gap: 2.5rem;
    }
    .brand-item {
      font-family: var(--heading-font);
      font-size: 1.4rem;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: rgba(255, 255, 255, 0.45);
      cursor: pointer;
      position: relative;
      padding-bottom: 6px;
      transition: all 0.4s ease;
    }
    .brand-item::after {
      content: "";
      position: absolute;
      bottom: 0;
      left: 0;
      width: 0%;
      height: 1px;
      background: var(--gold);
      transition: width 0.35s ease;
    }
    .brand-item:hover {
      color: #fff;
      transform: translateY(-2px);
    }
    .brand-item:hover::after {
      width: 100%;
    }

    /* Editorial Story Section */
    .story-section {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 5rem;
      align-items: center;
      padding: 8rem 4rem;
    }
    .story-img-frame {
      position: relative;
      max-width: 440px;
      width: 100%;
      height: 470px;
      justify-self: center;
      margin: 0 auto;
      border-radius: 24px;
      overflow: hidden;
      border: 1px solid var(--glass-border);
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.55), 0 0 30px rgba(212, 175, 112, 0.08);
    }
    .story-img-frame img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      filter: brightness(0.9);
      transition: transform 1s ease;
    }
    .story-img-frame:hover img {
      transform: scale(1.05);
    }
    .story-content {
      padding-right: 2rem;
    }
    .story-quote {
      font-size: clamp(2rem, 3.5vw, 3rem);
      line-height: 1.2;
      color: #fff;
      margin-bottom: 2rem;
    }
    .story-text {
      font-size: 1.05rem;
      color: var(--muted-color);
      line-height: 1.8;
      margin-bottom: 2.5rem;
    }

    /* Reviews / Testimonials Carousel */
    .testimonials-wrap {
      max-width: 820px;
      margin: 0 auto;
      text-align: center;
      position: relative;
    }
    .testimonial-slide {
      padding: 2rem;
      display: none;
    }
    .testimonial-slide.active {
      display: block;
      animation: fadeIn 0.6s ease;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .testimonial-stars {
      color: var(--gold);
      font-size: 1.1rem;
      letter-spacing: 4px;
      margin-bottom: 1.5rem;
    }
    .testimonial-quote {
      font-size: clamp(1.4rem, 2.5vw, 2.1rem);
      line-height: 1.4;
      font-family: var(--heading-font);
      font-style: italic;
      color: #fff;
      margin-bottom: 1.75rem;
    }
    .testimonial-author {
      font-family: var(--nav-font);
      font-size: 0.95rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--cream);
    }
    .testimonial-verified {
      font-size: 0.75rem;
      color: var(--gold);
      letter-spacing: 0.1em;
      text-transform: uppercase;
      margin-top: 4px;
    }
    .testimonial-controls {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 1.5rem;
      margin-top: 2.5rem;
    }
    .carousel-nav-btn {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: var(--glass-bg);
      border: 1px solid var(--glass-border);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: var(--trans-smooth);
    }
    .carousel-nav-btn:hover {
      border-color: var(--gold);
      background: rgba(212, 175, 112, 0.15);
      color: var(--gold);
    }

    /* Luxury Footer */
    .footer {
      background: #040404;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding: 6rem 4rem 3rem 4rem;
      position: relative;
    }
    .footer-top-grid {
      display: grid;
      grid-template-columns: 1.5fr 1fr 1fr 1fr 1.5fr;
      gap: 3.5rem;
      margin-bottom: 5rem;
    }
    .footer-brand-col .brand-title {
      font-size: 2rem;
      letter-spacing: 0.2em;
      margin-bottom: 0.5rem;
    }
    .footer-brand-col .brand-sub {
      font-family: var(--nav-font);
      font-size: 0.75rem;
      letter-spacing: 0.3em;
      text-transform: uppercase;
      color: var(--gold);
      margin-bottom: 1.5rem;
    }
    .footer-brand-col p {
      color: var(--muted-color);
      font-size: 0.9rem;
      line-height: 1.7;
    }
    .footer-col-heading {
      font-family: var(--nav-font);
      font-size: 0.78rem;
      letter-spacing: 0.25em;
      text-transform: uppercase;
      color: #fff;
      margin-bottom: 1.5rem;
    }
    .footer-links-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.8rem;
    }
    .footer-links-list a {
      color: var(--muted-color);
      text-decoration: none;
      font-size: 0.85rem;
      transition: color 0.3s ease, transform 0.3s ease;
      display: inline-block;
    }
    .footer-links-list a:hover {
      color: var(--gold-light);
      transform: translateX(4px);
    }
    .newsletter-form {
      display: flex;
      margin-top: 1rem;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--glass-border);
      border-radius: 100px;
      padding: 4px 6px;
    }
    .newsletter-input {
      flex: 1;
      background: transparent;
      border: none;
      color: #fff;
      padding: 0.65rem 1.25rem;
      font-family: var(--body-font);
      font-size: 0.85rem;
      outline: none;
    }
    .newsletter-submit-btn {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: var(--gold);
      color: #070707;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      transition: transform 0.3s ease, background 0.3s ease;
    }
    .newsletter-submit-btn:hover {
      transform: scale(1.08);
      background: var(--gold-light);
    }
    .footer-bottom-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 2.5rem;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      font-size: 0.8rem;
      color: rgba(255, 255, 255, 0.4);
      font-family: var(--nav-font);
    }

    /* Slide-out Drawer: Cart */
    .drawer-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(8px);
      z-index: 1000;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.4s ease;
    }
    .drawer-overlay.active {
      opacity: 1;
      pointer-events: auto;
    }
    .drawer-panel {
      position: fixed;
      top: 0;
      right: 0;
      width: 440px;
      max-width: 90vw;
      height: 100vh;
      background: #090909;
      border-left: 1px solid var(--glass-border);
      box-shadow: -20px 0 60px rgba(0, 0, 0, 0.8);
      z-index: 1001;
      display: flex;
      flex-direction: column;
      transform: translateX(100%);
      transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .drawer-panel.active {
      transform: translateX(0);
    }
    .drawer-header {
      padding: 1.75rem 2rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }
    .drawer-title {
      font-size: 1.4rem;
      color: #fff;
    }
    .close-drawer-btn {
      background: none;
      border: none;
      color: var(--muted-color);
      cursor: pointer;
      font-size: 1.5rem;
      transition: color 0.3s ease;
    }
    .close-drawer-btn:hover {
      color: #fff;
    }
    .drawer-body {
      flex: 1;
      overflow-y: auto;
      padding: 1.5rem 2rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }
    .cart-item-row {
      display: flex;
      gap: 1.25rem;
      padding-bottom: 1.25rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
      position: relative;
    }
    .cart-item-img {
      width: 70px;
      height: 70px;
      border-radius: 10px;
      background: rgba(255, 255, 255, 0.04);
      padding: 5px;
      object-fit: contain;
    }
    .cart-item-details {
      flex: 1;
    }
    .cart-item-brand {
      font-size: 0.65rem;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: var(--gold);
      font-family: var(--nav-font);
    }
    .cart-item-name {
      font-size: 1.05rem;
      color: #fff;
      margin-bottom: 0.2rem;
    }
    .cart-item-variant {
      font-size: 0.75rem;
      color: var(--muted-color);
      margin-bottom: 0.5rem;
    }
    .cart-item-qty-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .qty-controls {
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--glass-border);
      border-radius: 100px;
      padding: 2px 8px;
    }
    .qty-btn {
      background: none;
      border: none;
      color: #fff;
      cursor: pointer;
      padding: 0 4px;
      font-size: 0.9rem;
    }
    .qty-val {
      font-size: 0.8rem;
      font-family: var(--nav-font);
    }
    .cart-item-price {
      font-weight: 600;
      color: #fff;
      font-family: var(--nav-font);
    }
    .drawer-footer {
      padding: 1.75rem 2rem;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      background: #060606;
    }
    .subtotal-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1.25rem;
    }
    .subtotal-label {
      font-size: 0.95rem;
      color: var(--muted-color);
    }
    .subtotal-value {
      font-size: 1.35rem;
      font-weight: 600;
      color: #fff;
      font-family: var(--nav-font);
    }
    .checkout-btn {
      width: 100%;
      padding: 1rem;
      border-radius: 100px;
      background: var(--accent);
      color: #1b0a12;
      border: none;
      font-family: var(--nav-font);
      font-size: 0.88rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      font-weight: 700;
      cursor: pointer;
      transition: var(--trans-smooth);
    }
    .checkout-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 10px 30px rgba(251, 207, 232, 0.35);
    }

    /* Product Detail Fullscreen Modal */
    .product-modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(4, 4, 4, 0.88);
      backdrop-filter: blur(25px);
      -webkit-backdrop-filter: blur(25px);
      z-index: 2000;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 2rem;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.4s ease;
    }
    .product-modal-backdrop.active {
      opacity: 1;
      pointer-events: auto;
    }
    .product-modal-card {
      background: #090909;
      border: 1px solid var(--glass-border);
      border-radius: 28px;
      max-width: 1080px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      display: grid;
      grid-template-columns: 1.1fr 1.2fr;
      position: relative;
      box-shadow: 0 40px 100px rgba(0, 0, 0, 0.85);
      transform: scale(0.92);
      transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .product-modal-backdrop.active .product-modal-card {
      transform: scale(1);
    }
    .modal-close-btn {
      position: absolute;
      top: 1.5rem;
      right: 1.5rem;
      width: 42px;
      height: 42px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--glass-border);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 10;
      transition: var(--trans-smooth);
    }
    .modal-close-btn:hover {
      background: rgba(255, 255, 255, 0.2);
      transform: rotate(90deg);
    }
    .modal-gallery-side {
      background: radial-gradient(circle, rgba(255, 255, 255, 0.05) 0%, transparent 70%);
      padding: 3rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      position: relative;
      border-right: 1px solid rgba(255, 255, 255, 0.08);
    }
    .modal-main-img {
      max-height: 400px;
      max-width: 100%;
      object-fit: contain;
      filter: drop-shadow(0 25px 35px rgba(0, 0, 0, 0.6));
    }
    .modal-content-side {
      padding: 3.5rem 3rem;
      display: flex;
      flex-direction: column;
    }
    .modal-brand {
      font-family: var(--nav-font);
      font-size: 0.8rem;
      letter-spacing: 0.3em;
      text-transform: uppercase;
      color: var(--gold);
      margin-bottom: 0.5rem;
    }
    .modal-title {
      font-size: 2.4rem;
      color: #fff;
      margin-bottom: 0.5rem;
    }
    .modal-rating-row {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 1.5rem;
    }
    .modal-price {
      font-size: 1.8rem;
      font-weight: 600;
      color: #fff;
      font-family: var(--nav-font);
      margin-bottom: 1.5rem;
    }
    .modal-desc {
      font-size: 0.95rem;
      color: var(--muted-color);
      line-height: 1.7;
      margin-bottom: 2rem;
    }

    /* Variant Selectors */
    .variant-group {
      margin-bottom: 1.5rem;
    }
    .variant-label {
      font-size: 0.75rem;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: var(--gold-light);
      font-family: var(--nav-font);
      margin-bottom: 0.6rem;
      display: block;
    }
    .variant-pills-row {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }
    .variant-pill {
      padding: 6px 16px;
      border-radius: 100px;
      background: var(--glass-bg);
      border: 1px solid var(--glass-border);
      color: var(--muted-color);
      font-family: var(--nav-font);
      font-size: 0.78rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      cursor: pointer;
      transition: var(--trans-smooth);
    }
    .variant-pill:hover, .variant-pill.active {
      color: #070707;
      background: var(--gold);
      border-color: var(--gold);
      font-weight: 600;
    }

    /* Fragrance Notes Pyramid */
    .pyramid-container {
      background: rgba(255, 255, 255, 0.025);
      border: 1px solid var(--glass-border);
      border-radius: 16px;
      padding: 1.5rem;
      margin: 1.5rem 0 2rem 0;
    }
    .pyramid-heading {
      font-size: 0.72rem;
      letter-spacing: 0.25em;
      text-transform: uppercase;
      color: var(--gold);
      font-family: var(--nav-font);
      margin-bottom: 1rem;
      display: block;
      text-align: center;
    }
    .pyramid-tier {
      margin-bottom: 0.85rem;
      padding-bottom: 0.85rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      display: flex;
      align-items: center;
      gap: 1rem;
    }
    .pyramid-tier:last-child {
      margin-bottom: 0;
      padding-bottom: 0;
      border-bottom: none;
    }
    .tier-label {
      width: 90px;
      font-size: 0.68rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--muted-color);
      font-family: var(--nav-font);
    }
    .tier-notes {
      font-size: 0.9rem;
      color: #fff;
      font-family: var(--heading-font);
    }

    .modal-actions-row {
      display: flex;
      align-items: center;
      gap: 1.25rem;
      margin-top: auto;
    }
    .modal-add-bag-btn {
      flex: 1;
      padding: 1rem;
      border-radius: 100px;
      background: var(--accent);
      color: #1b0a12;
      border: none;
      font-family: var(--nav-font);
      font-size: 0.88rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      font-weight: 700;
      cursor: pointer;
      transition: var(--trans-smooth);
    }
    .modal-add-bag-btn:hover {
      box-shadow: 0 10px 30px rgba(251, 207, 232, 0.35);
      transform: translateY(-2px);
    }
    .modal-wish-btn {
      padding: 1rem 1.75rem;
      border-radius: 100px;
      background: var(--glass-bg);
      border: 1px solid var(--glass-border);
      color: #fff;
      font-family: var(--nav-font);
      font-size: 0.82rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: var(--trans-smooth);
    }
    .modal-wish-btn:hover {
      border-color: #ff477e;
      color: #ff477e;
    }

    /* Fullscreen Search Overlay */
    .search-overlay {
      position: fixed;
      inset: 0;
      background: rgba(5, 5, 5, 0.95);
      backdrop-filter: blur(25px);
      -webkit-backdrop-filter: blur(25px);
      z-index: 3000;
      display: flex;
      flex-direction: column;
      padding: 6rem 4rem;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.4s ease;
    }
    .search-overlay.active {
      opacity: 1;
      pointer-events: auto;
    }
    .search-top-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      max-width: 860px;
      width: 100%;
      margin: 0 auto 3rem auto;
    }
    .search-input-wrap {
      max-width: 860px;
      width: 100%;
      margin: 0 auto 2.5rem auto;
      position: relative;
    }
    .search-input-field {
      width: 100%;
      background: transparent;
      border: none;
      border-bottom: 2px solid var(--glass-border);
      color: #fff;
      font-family: var(--heading-font);
      font-size: clamp(2rem, 4vw, 3.5rem);
      padding-bottom: 1rem;
      outline: none;
      transition: border-color 0.4s ease;
    }
    .search-input-field:focus {
      border-color: var(--gold);
    }
    .search-popular-tags {
      max-width: 860px;
      width: 100%;
      margin: 0 auto 3rem auto;
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }
    .search-tag-label {
      font-size: 0.78rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--muted-color);
      font-family: var(--nav-font);
      margin-right: 6px;
    }
    .search-tag-pill {
      padding: 6px 16px;
      border-radius: 100px;
      background: var(--glass-bg);
      border: 1px solid var(--glass-border);
      color: var(--cream);
      font-family: var(--nav-font);
      font-size: 0.78rem;
      cursor: pointer;
      transition: var(--trans-smooth);
    }
    .search-tag-pill:hover {
      background: var(--gold);
      color: #070707;
      border-color: var(--gold);
    }
    .search-results-grid {
      max-width: 1000px;
      width: 100%;
      margin: 0 auto;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.5rem;
      overflow-y: auto;
      max-height: 50vh;
      padding: 1rem 0;
    }

    /* Toast Notification */
    .toast-notice {
      position: fixed;
      bottom: 30px;
      right: 30px;
      background: rgba(18, 18, 18, 0.9);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--gold);
      border-radius: 100px;
      padding: 12px 24px;
      color: #fff;
      font-family: var(--nav-font);
      font-size: 0.85rem;
      letter-spacing: 0.05em;
      display: flex;
      align-items: center;
      gap: 10px;
      z-index: 99999;
      transform: translateY(100px);
      opacity: 0;
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.4s ease;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }
    .toast-notice.show {
      transform: translateY(0);
      opacity: 1;
    }

    /* Responsive Queries */
    @media (max-width: 1200px) {
      .hero-section {
        min-height: 100vh;
        height: 100vh;
        min-height: 100dvh;
        padding: 0;
      }
      .hero-campaign-full-img {
        object-position: center right;
      }
      .hero-left {
        max-width: 500px;
        padding-left: clamp(2rem, 5vw, 3.5rem);
      }
      .products-grid {
        grid-template-columns: repeat(3, 1fr);
      }
      .footer-top-grid {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    @media (max-width: 1300px) and (min-width: 901px) {
      .header {
        padding: 0 1.5rem;
        height: 58px;
      }
      .nav.glass {
        gap: 0.4rem;
        padding: 0.28rem 0.75rem;
      }
      .nav-item {
        font-size: 0.68rem;
        letter-spacing: 0.05em;
        padding: 3px 4px;
      }
    }

      @media (max-width: 900px) {
      /* Prevent horizontal scrolling glitches on mobile devices */
      html, body {
        overflow-x: hidden !important;
        width: 100% !important;
        position: relative;
      }

      .header {
        padding: 0 1rem;
        height: 60px;
      }
      .brand-name {
        font-size: 1.15rem;
        letter-spacing: 0.16em;
      }
      .nav.glass {
        display: none;
      }
      .hamburger-btn {
        display: flex;
      }
      .header-actions {
        gap: 0.5rem;
      }
      .header-actions .icon-button {
        width: 38px;
        height: 38px;
      }

      /* Hero Section Mobile Optimization */
      .hero-section {
        min-height: 100vh;
        height: auto;
        min-height: 100dvh;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        padding: 5.5rem 1.25rem 4.5rem 1.25rem;
        position: relative;
        overflow: hidden;
      }
      .hero-campaign-full-img {
        object-position: 65% 35%;
      }
      .hero-campaign-scrim {
        background: linear-gradient(
          180deg,
          rgba(6, 4, 3, 0.40) 0%,
          rgba(6, 4, 3, 0.25) 25%,
          rgba(6, 4, 3, 0.78) 55%,
          rgba(6, 4, 3, 0.98) 82%,
          rgba(6, 4, 3, 1) 100%
        );
      }
      .hero-left {
        padding: 0;
        text-align: left;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        max-width: 100%;
        z-index: 10;
      }
      .hero-heading {
        font-size: clamp(1.9rem, 7.2vw, 2.75rem);
        line-height: 1.16;
        margin-bottom: 0.85rem;
        word-break: break-word;
      }
      .hero-tagline {
        font-size: 0.92rem;
        line-height: 1.55;
        margin-bottom: 1.5rem;
        max-width: 100%;
      }
      .hero-category-badge-wrap {
        justify-content: flex-start;
        margin-bottom: 1rem;
        flex-wrap: wrap;
        gap: 6px;
      }
      .hero-actions {
        display: flex;
        flex-direction: column;
        width: 100%;
        gap: 0.75rem;
      }
      .hero-actions .primary-btn,
      .hero-actions .secondary-btn,
      .hero-actions button,
      .hero-actions a {
        width: 100%;
        justify-content: center;
        text-align: center;
        padding: 0.9rem 1.4rem;
        font-size: 0.85rem;
      }

      /* Hero Minimal Carousel Controls on Mobile */
      
    /* Hide fragrance aura text and hero arrow navbar completely */
    .hero-carousel-controls-bar,
    .theme-morph-bar,
    .hero-carousel-controls {
      display: none !important;
      visibility: hidden !important;
      opacity: 0 !important;
      pointer-events: none !important;
    }

    .hero-carousel-controls-bar {
        position: static;
        transform: none;
        margin-top: 1.5rem;
        width: 100%;
        justify-content: space-between;
        padding: 8px 16px;
        background: rgba(0, 0, 0, 0.55);
      }

      .theme-morph-bar {
        position: relative;
        bottom: auto;
        left: auto;
        margin-top: 1.5rem;
        width: 100%;
        max-width: 100%;
        flex-direction: column;
        align-items: flex-start;
        gap: 0.75rem;
        padding: 0;
      }
      .theme-pills {
        width: 100%;
        justify-content: flex-start;
        flex-wrap: wrap;
        gap: 6px;
      }

      .section-container {
        padding: 3.5rem 1.25rem;
      }
      .section-header {
        margin-bottom: 2.5rem;
      }
      .section-title {
        font-size: clamp(1.75rem, 6.5vw, 2.4rem);
        line-height: 1.2;
      }
      .section-subtitle {
        font-size: 0.88rem;
        line-height: 1.6;
      }

      /* Grid Responsiveness */
      .collections-grid,
      .products-grid,
      .ingredients-grid,
      .search-results-grid,
      .discovery-grid,
      .discovery-sets-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
      }
      .mood-cards-container {
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
      }
      .story-section {
        grid-template-columns: 1fr;
        gap: 2rem;
        padding: 3.5rem 1.25rem;
      }
      .story-img-frame {
        max-width: 100%;
        height: 320px;
      }
      .story-quote {
        font-size: clamp(1.3rem, 5vw, 1.8rem);
        line-height: 1.35;
      }

      /* Product Detail Modal Mobile */
      .product-modal-card {
        grid-template-columns: 1fr;
        max-height: 92vh;
        border-radius: 18px;
        margin: 0.5rem;
      }
      .modal-gallery-side {
        border-right: none;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        padding: 1.5rem;
      }
      .modal-info-side {
        padding: 1.5rem 1.25rem;
      }
      .modal-product-img {
        max-height: 240px;
        object-fit: contain;
      }

      /* Drawer Panels Mobile Full View */
      .drawer-panel {
        width: 100vw !important;
        max-width: 100vw !important;
      }

      /* Footer Top Grid */
      .footer-top-grid {
        grid-template-columns: 1fr;
        gap: 2rem;
      }

      /* Custom Touch Cursor Off */
      .custom-cursor, .custom-cursor-follower {
        display: none !important;
      }

      /* Floating Compare Tray Mobile */
      .floating-compare-tray {
        width: calc(100% - 1.5rem);
        bottom: 12px;
        padding: 10px 14px;
        border-radius: 16px;
      }
      .compare-modal-card {
        padding: 1.5rem 1rem;
        border-radius: 16px;
        margin: 0.5rem;
        max-height: 92vh;
      }
    }

    @media (max-width: 600px) {
      .collections-grid,
      .products-grid,
      .ingredients-grid,
      .mood-cards-container,
      .search-results-grid,
      .discovery-grid,
      .discovery-sets-grid {
        grid-template-columns: 1fr;
      }
      .hero-heading {
        font-size: clamp(1.75rem, 8vw, 2.3rem);
        line-height: 1.18;
      }
      .hero-right-stage {
        height: 280px;
      }
      .product-card {
        flex: 0 0 92% !important;
      }
      .carousel-track-container {
        padding: 0.5rem 0;
      }

      /* Checkout & Payment Modals Mobile Polish */
      .checkout-modal-card,
      .payment-modal-card,
      .order-success-card,
      .track-order-card {
        padding: 1.75rem 1.15rem !important;
        border-radius: 16px !important;
        max-height: 94vh !important;
      }
      .modal-close-btn {
        top: 1rem !important;
        right: 1rem !important;
        width: 36px !important;
        height: 36px !important;
      }
      .checkout-grid {
        grid-template-columns: 1fr !important;
        gap: 1.5rem !important;
      }

      /* Studio & Steppers Mobile */
      .studio-step-indicators {
        flex-wrap: wrap;
        gap: 6px;
      }
      .step-indicator-pill {
        font-size: 0.7rem;
        padding: 4px 10px;
      }
      .notes-selector-grid {
        grid-template-columns: 1fr 1fr;
        gap: 8px;
      }
    }

    /* ==========================================================
       MYOP (MAKE YOUR OWN PERFUME) & LUXURY ADD-ONS STYLING
       ========================================================== */

    /* Top Announcement Bar */
    .top-announcement-bar {
      background: linear-gradient(90deg, #110d08 0%, #201509 50%, #110d08 100%);
      border-bottom: 1px solid rgba(212, 175, 112, 0.25);
      color: var(--cream);
      font-family: var(--nav-font);
      font-size: 0.72rem;
      letter-spacing: 0.12em;
      padding: 7px 1.5rem;
      position: relative;
      z-index: 101;
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
    }
    .announcement-left {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .announcement-badge {
      background: var(--gold);
      color: #000;
      font-size: 0.65rem;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 999px;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }
    .announcement-text {
      color: rgba(255, 255, 255, 0.88);
    }
    .announcement-right {
      display: flex;
      align-items: center;
      gap: 16px;
    }
    .announcement-link {
      color: var(--gold);
      text-decoration: none;
      font-size: 0.72rem;
      transition: color 0.2s ease;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    .announcement-link:hover {
      color: #fff;
      text-decoration: underline;
    }

    /* MYOP Blending Studio Section */
    .myop-studio-section {
      position: relative;
      padding: 6.5rem 2rem;
      max-width: 1400px;
      margin: 0 auto;
    }
    .myop-hero-banner {
      background: linear-gradient(135deg, rgba(212, 175, 112, 0.08) 0%, rgba(100, 21, 45, 0.12) 100%);
      border: 1px solid rgba(212, 175, 112, 0.25);
      border-radius: 16px;
      padding: 3rem 2.5rem;
      margin-bottom: 3.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 2rem;
      position: relative;
      overflow: hidden;
    }
    .myop-hero-banner::after {
      content: '';
      position: absolute;
      top: -50%;
      right: -10%;
      width: 400px;
      height: 400px;
      background: radial-gradient(circle, rgba(212, 175, 112, 0.15) 0%, transparent 70%);
      pointer-events: none;
    }
    .myop-banner-content h3 {
      font-family: var(--heading-font);
      font-size: 2.2rem;
      font-weight: 500;
      color: #fff;
      margin-bottom: 0.8rem;
    }
    .myop-banner-content p {
      font-size: 0.95rem;
      color: var(--muted-color);
      max-width: 620px;
      line-height: 1.6;
    }
    .tropical-badge-large {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: rgba(212, 175, 112, 0.12);
      border: 1px solid var(--gold);
      padding: 10px 18px;
      border-radius: 999px;
      color: var(--gold-light);
      font-family: var(--nav-font);
      font-size: 0.82rem;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      font-weight: 600;
      margin-top: 1.2rem;
    }

    .myop-studio-grid {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 3.5rem;
      align-items: start;
    }

    .studio-panel {
      background: rgba(18, 18, 18, 0.7);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--glass-border);
      border-radius: 16px;
      padding: 2.5rem;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
    }

    /* Studio Stepper Bar */
    .studio-stepper-nav {
      display: flex;
      align-items: center;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      margin-bottom: 2rem;
      padding-bottom: 1rem;
      gap: 1rem;
      overflow-x: auto;
    }
    .studio-step-tab {
      background: transparent;
      border: none;
      color: rgba(255, 255, 255, 0.5);
      font-family: var(--nav-font);
      font-size: 0.78rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      font-weight: 600;
      padding: 6px 12px;
      cursor: pointer;
      position: relative;
      white-space: nowrap;
      transition: var(--trans-smooth);
      border-radius: 6px;
    }
    .studio-step-tab:hover {
      color: #fff;
    }
    .studio-step-tab.active {
      color: var(--gold);
      background: rgba(212, 175, 112, 0.1);
    }
    .studio-step-tab.active::after {
      content: '';
      position: absolute;
      bottom: -1rem;
      left: 10%;
      width: 80%;
      height: 2px;
      background: var(--gold);
    }

    /* Step 1: Flacon Sizes */
    .flacon-picker-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.2rem;
      margin-bottom: 1.5rem;
    }
    .flacon-choice-card {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 1.4rem 1rem;
      text-align: center;
      cursor: pointer;
      transition: var(--trans-smooth);
      position: relative;
    }
    .flacon-choice-card:hover {
      border-color: rgba(212, 175, 112, 0.4);
      transform: translateY(-2px);
    }
    .flacon-choice-card.selected {
      border-color: var(--gold);
      background: rgba(212, 175, 112, 0.08);
      box-shadow: 0 0 20px rgba(212, 175, 112, 0.15);
    }
    .flacon-choice-card.selected::before {
      content: '✓';
      position: absolute;
      top: 10px;
      right: 10px;
      color: var(--gold);
      font-size: 0.8rem;
      font-weight: 700;
    }
    .flacon-popular-badge {
      position: absolute;
      top: -10px;
      left: 50%;
      transform: translateX(-50%);
      background: var(--gold);
      color: #000;
      font-size: 0.6rem;
      font-weight: 800;
      padding: 2px 8px;
      border-radius: 999px;
      letter-spacing: 0.08em;
      white-space: nowrap;
    }
    .flacon-icon-svg {
      width: 38px;
      height: 52px;
      margin: 0 auto 0.8rem auto;
      display: block;
      color: var(--gold);
    }
    .flacon-size-title {
      font-family: var(--heading-font);
      font-size: 1.15rem;
      color: #fff;
      margin-bottom: 4px;
    }
    .flacon-size-desc {
      font-size: 0.75rem;
      color: var(--muted-color);
      margin-bottom: 8px;
    }
    .flacon-size-price {
      font-family: var(--nav-font);
      font-weight: 700;
      color: var(--gold);
      font-size: 1.05rem;
    }

    /* Flacon Color Finish */
    .finish-selector-row {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-top: 1.5rem;
    }
    .finish-pill-btn {
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 999px;
      padding: 6px 14px;
      color: rgba(255, 255, 255, 0.8);
      font-size: 0.78rem;
      font-family: var(--nav-font);
      cursor: pointer;
      transition: var(--trans-smooth);
    }
    .finish-pill-btn.selected {
      border-color: var(--gold);
      background: rgba(212, 175, 112, 0.1);
      color: #fff;
    }
    .finish-dot {
      width: 12px;
      height: 12px;
      border-radius: 50%;
      border: 1px solid rgba(255, 255, 255, 0.3);
    }

    /* Step 2: Base Oils Grid */
    .oils-selector-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 1rem;
      max-height: 380px;
      overflow-y: auto;
      padding-right: 6px;
    }
    .oil-card {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 10px;
      padding: 1.1rem;
      cursor: pointer;
      transition: var(--trans-smooth);
      position: relative;
    }
    .oil-card:hover {
      border-color: rgba(212, 175, 112, 0.4);
      background: rgba(255, 255, 255, 0.05);
    }
    .oil-card.selected {
      border-color: var(--gold);
      background: rgba(212, 175, 112, 0.09);
      box-shadow: 0 0 15px rgba(212, 175, 112, 0.15);
    }
    .oil-card.selected::after {
      content: '✓';
      position: absolute;
      top: 10px;
      right: 10px;
      color: var(--gold);
      font-weight: 700;
    }
    .oil-origin-label {
      font-size: 0.65rem;
      font-family: var(--nav-font);
      letter-spacing: 0.1em;
      color: var(--gold);
      text-transform: uppercase;
      display: block;
      margin-bottom: 4px;
    }
    .oil-card-title {
      font-family: var(--heading-font);
      font-size: 1.05rem;
      color: #fff;
      margin-bottom: 6px;
    }
    .oil-card-desc {
      font-size: 0.72rem;
      color: var(--muted-color);
      line-height: 1.4;
      margin-bottom: 8px;
    }
    .oil-tag-pill {
      font-size: 0.65rem;
      background: rgba(255, 255, 255, 0.08);
      padding: 3px 8px;
      border-radius: 999px;
      color: rgba(255, 255, 255, 0.8);
      display: inline-block;
    }

    /* Step 3: Heart & Accent Notes */
    .heart-notes-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
      gap: 0.8rem;
    }
    .heart-note-pill {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 8px;
      padding: 0.8rem;
      cursor: pointer;
      text-align: center;
      transition: var(--trans-smooth);
    }
    .heart-note-pill:hover {
      border-color: rgba(212, 175, 112, 0.4);
    }
    .heart-note-pill.selected {
      background: rgba(212, 175, 112, 0.12);
      border-color: var(--gold);
      color: #fff;
    }
    .heart-note-pill.selected .heart-note-icon {
      color: var(--gold);
    }
    .heart-note-icon {
      font-size: 1.2rem;
      margin-bottom: 4px;
      display: block;
    }
    .heart-note-name {
      font-size: 0.78rem;
      font-weight: 500;
      color: #fff;
    }
    .heart-note-family {
      font-size: 0.65rem;
      color: var(--muted-color);
    }

    /* Step 4: Blending Ratio & Oil Concentration Guarantee */
    .ratio-slider-box {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      padding: 1.8rem;
      margin-bottom: 1.8rem;
    }
    .ratio-labels-row {
      display: flex;
      justify-content: space-between;
      margin-bottom: 0.8rem;
      font-family: var(--nav-font);
      font-size: 0.82rem;
      color: var(--cream);
    }
    .ratio-slider-input {
      width: 100%;
      height: 8px;
      border-radius: 4px;
      background: linear-gradient(90deg, var(--gold) var(--slider-pct, 60%), rgba(255, 255, 255, 0.15) var(--slider-pct, 60%));
      outline: none;
      -webkit-appearance: none;
      cursor: pointer;
      margin-bottom: 1.2rem;
    }
    .ratio-slider-input::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: var(--gold);
      border: 3px solid #000;
      box-shadow: 0 0 10px rgba(212, 175, 112, 0.6);
      cursor: pointer;
    }
    .ratio-breakdown-metrics {
      display: flex;
      justify-content: space-around;
      padding-top: 1rem;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      text-align: center;
    }
    .metric-item-val {
      font-family: var(--nav-font);
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--gold);
    }
    .metric-item-lbl {
      font-size: 0.7rem;
      color: var(--muted-color);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .oil-guarantee-card {
      background: linear-gradient(135deg, rgba(212, 175, 112, 0.1) 0%, rgba(20, 20, 20, 0.6) 100%);
      border: 1px solid var(--gold);
      border-radius: 12px;
      padding: 1.5rem;
      display: flex;
      align-items: center;
      gap: 1.2rem;
      margin-top: 1.5rem;
    }
    .oil-guarantee-icon {
      width: 50px;
      height: 50px;
      flex-shrink: 0;
      border-radius: 50%;
      background: rgba(212, 175, 112, 0.2);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--gold);
      font-size: 1.4rem;
    }
    .oil-guarantee-info h4 {
      font-family: var(--nav-font);
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--gold-light);
      margin-bottom: 4px;
      letter-spacing: 0.04em;
    }
    .oil-guarantee-info p {
      font-size: 0.78rem;
      color: var(--muted-color);
      line-height: 1.4;
    }

    /* Step 5: Name & Laser Engraving */
    .custom-name-field-wrap {
      margin-bottom: 1.5rem;
    }
    .custom-field-label {
      display: block;
      font-family: var(--nav-font);
      font-size: 0.8rem;
      letter-spacing: 0.1em;
      color: var(--cream);
      text-transform: uppercase;
      margin-bottom: 0.6rem;
    }
    .custom-text-input {
      width: 100%;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.18);
      border-radius: 8px;
      padding: 12px 16px;
      color: #fff;
      font-family: var(--heading-font);
      font-size: 1.15rem;
      outline: none;
      transition: var(--trans-smooth);
    }
    .custom-text-input:focus {
      border-color: var(--gold);
      box-shadow: 0 0 15px rgba(212, 175, 112, 0.2);
    }
    .engrave-toggle-row {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-top: 1rem;
      margin-bottom: 1.5rem;
    }

    /* Flacon Visualizer Side (Sticky Right) */
    .flacon-visualizer-sticky {
      position: sticky;
      top: 100px;
      background: rgba(14, 14, 14, 0.75);
      backdrop-filter: blur(25px);
      -webkit-backdrop-filter: blur(25px);
      border: 1px solid var(--glass-border);
      border-radius: 16px;
      padding: 2.5rem;
      text-align: center;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6);
    }
    .flacon-visualizer-glass {
      position: relative;
      width: 240px;
      height: 340px;
      margin: 0 auto 2rem auto;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .flacon-rendered-bottle {
      width: 100%;
      height: 100%;
      object-fit: contain;
      filter: drop-shadow(0 20px 30px rgba(0, 0, 0, 0.7));
      transition: filter 0.5s ease;
    }
    .flacon-tint-layer {
      position: absolute;
      top: 25%;
      left: 20%;
      width: 60%;
      height: 55%;
      border-radius: 12px;
      mix-blend-mode: color;
      pointer-events: none;
      transition: background 0.6s ease;
      background: radial-gradient(circle, rgba(212, 175, 112, 0.4) 0%, rgba(100, 21, 45, 0.3) 100%);
    }
    .flacon-engraving-rendered {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 70%;
      text-align: center;
      pointer-events: none;
      color: var(--gold);
      text-shadow: 0 1px 3px rgba(0, 0, 0, 0.9), 0 0 8px rgba(212, 175, 112, 0.4);
      font-size: 1rem;
      letter-spacing: 0.1em;
      font-weight: 600;
      transition: all 0.3s ease;
      word-break: break-word;
    }

    .formula-breakdown-card {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 10px;
      padding: 1.2rem;
      text-align: left;
      margin-bottom: 1.5rem;
    }
    .formula-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.8rem;
      color: var(--muted-color);
      margin-bottom: 6px;
    }
    .formula-row strong {
      color: #fff;
    }
    .batch-id-chip {
      display: inline-block;
      font-family: var(--nav-font);
      font-size: 0.68rem;
      color: var(--gold);
      background: rgba(212, 175, 112, 0.1);
      padding: 2px 8px;
      border-radius: 4px;
      border: 1px solid rgba(212, 175, 112, 0.2);
    }
    .custom-blend-price-row {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      margin-bottom: 1.2rem;
    }
    .custom-blend-price {
      font-family: var(--heading-font);
      font-size: 2rem;
      color: var(--gold);
    }
    .custom-blend-oil-tag {
      font-family: var(--nav-font);
      font-size: 0.75rem;
      color: #86efac;
      letter-spacing: 0.05em;
    }

    /* ==========================================================
       BOTTLE PERSONALISATION & LASER ENGRAVING STUDIO
       ========================================================== */
    .personalise-studio-section {
      padding: 6rem 2rem;
      max-width: 1400px;
      margin: 0 auto;
    }
    .personalise-studio-card {
      background: linear-gradient(145deg, rgba(22, 22, 22, 0.8) 0%, rgba(10, 10, 10, 0.95) 100%);
      border: 1px solid rgba(212, 175, 112, 0.28);
      border-radius: 20px;
      padding: 3.5rem;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 3.5rem;
      align-items: center;
      position: relative;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.7);
    }
    .engrave-visualizer-wrap {
      position: relative;
      background: radial-gradient(circle, rgba(212, 175, 112, 0.08) 0%, transparent 70%);
      border-radius: 16px;
      padding: 2rem;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }
    .engrave-flacon-img-stage {
      position: relative;
      width: 270px;
      aspect-ratio: 896 / 1200;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .engrave-flacon-img-stage img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      display: block;
      filter: drop-shadow(0 25px 35px rgba(0, 0, 0, 0.8));
    }
    .live-engraved-plate {
      position: absolute;
      top: 60%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 54%;
      max-width: 155px;
      padding: 7px 8px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      background: rgba(8, 14, 28, 0.45);
      border: 1px solid rgba(212, 175, 112, 0.55);
      border-radius: 4px;
      box-shadow: inset 0 0 12px rgba(0, 0, 0, 0.6), 0 4px 18px rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(1.5px);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      box-sizing: border-box;
      pointer-events: none;
      z-index: 5;
    }
    .live-engraved-text {
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      line-height: 1.3;
      display: block;
      width: 100%;
      text-align: center;
      overflow-wrap: break-word;
      word-wrap: break-word;
      hyphens: auto;
      transition: all 0.3s ease;
      color: #e6c88b;
      text-shadow: 0 1px 3px rgba(0, 0, 0, 0.95), 0 0 8px rgba(212, 175, 112, 0.6);
    }

    /* Font choice pills */
    .engrave-font-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
      margin-bottom: 1.5rem;
    }
    .engrave-font-btn {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 8px;
      padding: 10px 14px;
      color: rgba(255, 255, 255, 0.8);
      cursor: pointer;
      text-align: left;
      transition: var(--trans-smooth);
    }
    .engrave-font-btn:hover {
      border-color: rgba(212, 175, 112, 0.4);
    }
    .engrave-font-btn.selected {
      border-color: var(--gold);
      background: rgba(212, 175, 112, 0.12);
      color: #fff;
    }
    .font-sample-preview {
      font-size: 1.05rem;
      margin-bottom: 2px;
      display: block;
      color: var(--gold);
    }
    .font-name-label {
      font-size: 0.68rem;
      font-family: var(--nav-font);
      color: var(--muted-color);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* Foil Finishes */
    .foil-finishes-row {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 1.8rem;
    }
    .foil-btn {
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 999px;
      padding: 6px 14px;
      color: rgba(255, 255, 255, 0.85);
      font-size: 0.78rem;
      font-family: var(--nav-font);
      cursor: pointer;
      transition: var(--trans-smooth);
    }
    .foil-btn.selected {
      border-color: var(--gold);
      background: rgba(212, 175, 112, 0.15);
      color: #fff;
    }
    .foil-swatch {
      width: 14px;
      height: 14px;
      border-radius: 50%;
      border: 1px solid rgba(255, 255, 255, 0.4);
    }

    /* ==========================================================
       DISCOVERY SETS & SAMPLE KITS
       ========================================================== */
    .discovery-section {
      padding: 6rem 2rem;
      max-width: 1380px;
      margin: 0 auto;
      position: relative;
    }
    .discovery-grid,
    .discovery-sets-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 2.5rem;
      align-items: stretch;
      margin-top: 3rem;
    }
    .discovery-card {
      background: linear-gradient(180deg, rgba(255, 255, 255, 0.04) 0%, rgba(18, 22, 32, 0.85) 100%);
      border: 1px solid rgba(212, 175, 112, 0.22);
      border-radius: 16px;
      overflow: hidden;
      transition: all 0.45s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      display: flex;
      flex-direction: column;
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.5);
    }
    .discovery-card:hover {
      transform: translateY(-8px);
      border-color: rgba(212, 175, 112, 0.6);
      box-shadow: 0 24px 50px rgba(0, 0, 0, 0.75), 0 0 25px rgba(212, 175, 112, 0.15);
    }
    .discovery-img-wrap,
    .discovery-card-media {
      position: relative;
      width: 100%;
      height: 270px;
      background: #080c14;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 0;
      box-sizing: border-box;
      border-bottom: 1px solid rgba(212, 175, 112, 0.18);
    }
    .discovery-img-wrap::after,
    .discovery-card-media::after {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(to bottom, rgba(0,0,0,0.15) 0%, transparent 45%, rgba(12, 16, 24, 0.9) 100%);
      pointer-events: none;
      z-index: 1;
    }
    .discovery-img,
    .discovery-card-media img {
      width: 100%;
      height: 100%;
      max-height: 100%;
      object-fit: cover;
      object-position: center;
      transition: transform 0.65s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .discovery-card:hover .discovery-img,
    .discovery-card:hover .discovery-card-media img {
      transform: scale(1.06);
    }
    .cashback-badge,
    .cashback-banner-tag {
      position: absolute;
      top: 14px;
      left: 14px;
      background: linear-gradient(135deg, #d4af70 0%, #f6e6be 50%, #b89146 100%);
      color: #0b0f17;
      font-family: var(--nav-font);
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 0.08em;
      padding: 5px 12px;
      border-radius: 999px;
      text-transform: uppercase;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.6);
      z-index: 2;
    }
    .discovery-body,
    .discovery-card-body {
      padding: 1.8rem;
      display: flex;
      flex-direction: column;
      flex: 1;
    }
    .discovery-badge {
      display: inline-block;
      align-self: flex-start;
      font-size: 0.7rem;
      font-family: var(--nav-font);
      text-transform: uppercase;
      letter-spacing: 0.14em;
      color: var(--gold-light);
      background: rgba(212, 175, 112, 0.12);
      border: 1px solid rgba(212, 175, 112, 0.25);
      border-radius: 999px;
      padding: 4px 10px;
      margin-bottom: 0.75rem;
    }
    .discovery-title,
    .discovery-card-title {
      font-family: var(--heading-font);
      font-size: 1.4rem;
      letter-spacing: 0.03em;
      color: #fff;
      margin-bottom: 0.6rem;
      line-height: 1.3;
    }
    .discovery-desc,
    .discovery-card-desc {
      font-size: 0.86rem;
      color: var(--muted-color);
      line-height: 1.6;
      margin-bottom: 1.3rem;
      flex: 1;
    }
    .vials-row,
    .vials-included-list {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 10px;
      padding: 10px 12px;
      margin-bottom: 1.5rem;
      display: flex;
      flex-wrap: wrap;
      gap: 7px;
    }
    .vial-pill {
      background: rgba(212, 175, 112, 0.14);
      border: 1px solid rgba(212, 175, 112, 0.28);
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.72rem;
      font-family: var(--nav-font);
      letter-spacing: 0.04em;
      color: var(--gold-light);
      white-space: nowrap;
      transition: all 0.25s ease;
      cursor: pointer;
    }
    .vial-pill:hover {
      background: var(--gold);
      color: #070707;
      border-color: var(--gold);
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(212, 175, 112, 0.3);
    }
    .discovery-price-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: auto;
      padding-top: 1rem;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
    }
    .discovery-price {
      font-family: var(--heading-font);
      font-size: 1.45rem;
      color: var(--gold-light);
      font-weight: 700;
      letter-spacing: 0.02em;
      margin-right: 8px;
    }
    .discovery-orig-price {
      font-size: 0.85rem;
      color: var(--muted-color);
      text-decoration: line-through;
    }

    /* ==========================================================
       SCENT DEALS & BUNDLE OFFERS
       ========================================================== */
    .deals-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 2rem;
    }
    .deal-card {
      background: linear-gradient(145deg, rgba(255, 255, 255, 0.04) 0%, rgba(100, 21, 45, 0.08) 100%);
      border: 1px solid rgba(212, 175, 112, 0.22);
      border-radius: 14px;
      padding: 2rem;
      position: relative;
      transition: var(--trans-smooth);
    }
    .deal-card:hover {
      border-color: var(--gold);
      transform: translateY(-4px);
    }
    .deal-badge-pill {
      display: inline-block;
      background: var(--wine);
      border: 1px solid rgba(212, 175, 112, 0.4);
      color: var(--gold-light);
      font-family: var(--nav-font);
      font-size: 0.68rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      padding: 3px 10px;
      border-radius: 999px;
      text-transform: uppercase;
      margin-bottom: 1rem;
    }
    .deal-title {
      font-family: var(--heading-font);
      font-size: 1.5rem;
      color: #fff;
      margin-bottom: 0.6rem;
    }
    .deal-desc {
      font-size: 0.85rem;
      color: var(--muted-color);
      line-height: 1.5;
      margin-bottom: 1.2rem;
    }
    .coupon-code-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(0, 0, 0, 0.5);
      border: 1px dashed var(--gold);
      border-radius: 6px;
      padding: 6px 12px;
      color: var(--gold);
      font-family: monospace;
      font-size: 0.95rem;
      font-weight: 700;
      cursor: pointer;
      transition: var(--trans-smooth);
    }
    .coupon-code-pill:hover {
      background: rgba(212, 175, 112, 0.15);
    }

    /* ==========================================================
       PERFUME BAR STORE LOCATOR (68+ STORES ACROSS INDIA)
       ========================================================== */
    .stores-section {
      padding: 6.5rem 2rem;
      max-width: 1400px;
      margin: 0 auto;
    }
    .city-filter-bar {
      display: flex;
      align-items: center;
      gap: 10px;
      overflow-x: auto;
      padding-bottom: 1.2rem;
      margin-bottom: 2rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }
    .city-pill-btn {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 999px;
      padding: 8px 18px;
      color: rgba(255, 255, 255, 0.8);
      font-family: var(--nav-font);
      font-size: 0.82rem;
      white-space: nowrap;
      cursor: pointer;
      transition: var(--trans-smooth);
    }
    .city-pill-btn:hover {
      border-color: rgba(212, 175, 112, 0.4);
      color: #fff;
    }
    .city-pill-btn.active {
      background: var(--gold);
      border-color: var(--gold);
      color: #000;
      font-weight: 700;
    }
    .stores-cards-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.8rem;
    }
    .store-card {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 14px;
      padding: 1.8rem;
      display: flex;
      flex-direction: column;
      transition: var(--trans-smooth);
    }
    .store-card:hover {
      border-color: rgba(212, 175, 112, 0.4);
      transform: translateY(-3px);
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
    }
    .store-status-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.8rem;
    }
    .store-city-tag {
      font-family: var(--nav-font);
      font-size: 0.7rem;
      letter-spacing: 0.1em;
      color: var(--gold);
      text-transform: uppercase;
      font-weight: 700;
    }
    .store-status-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.72rem;
      color: #86efac;
      background: rgba(34, 197, 94, 0.1);
      padding: 3px 8px;
      border-radius: 999px;
    }
    .store-status-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #22c55e;
      box-shadow: 0 0 6px #22c55e;
    }
    .store-mall-title {
      font-family: var(--heading-font);
      font-size: 1.35rem;
      color: #fff;
      margin-bottom: 0.4rem;
    }
    .store-kiosk-desc {
      font-size: 0.82rem;
      color: var(--muted-color);
      line-height: 1.4;
      margin-bottom: 1rem;
    }
    .store-perks-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 1.4rem;
    }
    .store-perk-tag {
      font-size: 0.68rem;
      background: rgba(255, 255, 255, 0.06);
      border-radius: 4px;
      padding: 3px 8px;
      color: var(--cream);
    }
    .store-card-actions {
      display: flex;
      gap: 10px;
      margin-top: auto;
    }
    .store-book-btn {
      flex: 1;
      background: rgba(212, 175, 112, 0.12);
      border: 1px solid var(--gold);
      color: var(--gold-light);
      font-family: var(--nav-font);
      font-size: 0.75rem;
      font-weight: 600;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      padding: 9px 12px;
      border-radius: 6px;
      cursor: pointer;
      transition: var(--trans-smooth);
    }
    .store-book-btn:hover {
      background: var(--gold);
      color: #000;
    }
    .store-map-link {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #fff;
      padding: 9px 14px;
      border-radius: 6px;
      font-size: 0.75rem;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: var(--trans-smooth);
    }
    .store-map-link:hover {
      background: rgba(255, 255, 255, 0.12);
    }

    /* ==========================================================
       ECO-REFILL & SUSTAINABILITY SECTION
       ========================================================== */
    .refill-card-wrap {
      background: linear-gradient(135deg, rgba(7, 59, 53, 0.25) 0%, rgba(18, 18, 18, 0.8) 100%);
      border: 1px solid rgba(7, 59, 53, 0.6);
      border-radius: 18px;
      padding: 3.5rem;
      display: grid;
      grid-template-columns: 1.2fr 0.8fr;
      gap: 3rem;
      align-items: center;
    }
    .refill-steps-list {
      display: flex;
      flex-direction: column;
      gap: 1.4rem;
      margin-top: 1.8rem;
    }
    .refill-step-item {
      display: flex;
      align-items: flex-start;
      gap: 16px;
    }
    .refill-num-badge {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: var(--gold);
      color: #000;
      font-weight: 800;
      font-size: 0.85rem;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .refill-step-text h4 {
      font-family: var(--nav-font);
      font-size: 0.95rem;
      color: #fff;
      margin-bottom: 2px;
    }
    .refill-step-text p {
      font-size: 0.82rem;
      color: var(--muted-color);
      line-height: 1.4;
    }

    /* ==========================================================
       CORPORATE GIFTING & WEDDING FAVORS
       ========================================================== */
    .corporate-grid {
      display: grid;
      grid-template-columns: 1fr 1.1fr;
      gap: 3.5rem;
      align-items: center;
    }
    .corporate-form-panel {
      background: rgba(22, 22, 22, 0.7);
      backdrop-filter: blur(20px);
      border: 1px solid var(--glass-border);
      border-radius: 16px;
      padding: 2.5rem;
    }
    .corp-input-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin-bottom: 1.2rem;
    }

    /* ==========================================================
       MODALS: TRACK ORDER & STORE APPOINTMENT
       ========================================================== */
    .custom-feature-modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.82);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      z-index: 1000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }
    .custom-feature-modal-card {
      background: #111111;
      border: 1px solid var(--glass-border);
      border-radius: 16px;
      max-width: 580px;
      width: 100%;
      padding: 2.5rem;
      position: relative;
      box-shadow: 0 30px 70px rgba(0, 0, 0, 0.8);
      max-height: 90vh;
      overflow-y: auto;
    }

    /* Stepper for Order Tracking */
    .tracking-timeline {
      margin: 2rem 0;
      position: relative;
      padding-left: 2rem;
    }
    .tracking-timeline::before {
      content: '';
      position: absolute;
      left: 7px;
      top: 10px;
      bottom: 10px;
      width: 2px;
      background: rgba(255, 255, 255, 0.12);
    }
    .tracking-step-item {
      position: relative;
      margin-bottom: 1.6rem;
    }
    .tracking-step-dot {
      position: absolute;
      left: -2rem;
      top: 3px;
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: #222;
      border: 2px solid var(--gold);
    }
    .tracking-step-item.completed .tracking-step-dot {
      background: var(--gold);
      box-shadow: 0 0 10px rgba(212, 175, 112, 0.5);
    }
    .tracking-step-item.active .tracking-step-dot {
      background: #3b82f6;
      border-color: #60a5fa;
      box-shadow: 0 0 10px rgba(59, 130, 246, 0.6);
      animation: pulseGlow 1.5s infinite;
    }
    @keyframes pulseGlow {
      0%, 100% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.3); opacity: 0.7; }
    }
    .tracking-step-title {
      font-size: 0.95rem;
      font-weight: 600;
      color: #fff;
      margin-bottom: 2px;
    }
    .tracking-step-desc {
      font-size: 0.78rem;
      color: var(--muted-color);
    }

    /* PINCODE & CART ENHANCEMENTS */
    .pincode-box-wrap {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 8px;
      padding: 12px;
      margin: 1.2rem 0;
    }
    .pincode-input-row {
      display: flex;
      gap: 8px;
    }
    .pincode-input {
      flex: 1;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 6px;
      padding: 8px 12px;
      color: #fff;
      font-size: 0.85rem;
      font-family: var(--nav-font);
      outline: none;
    }
    .pincode-check-btn {
      background: var(--gold);
      color: #000;
      border: none;
      border-radius: 6px;
      padding: 8px 14px;
      font-family: var(--nav-font);
      font-size: 0.78rem;
      font-weight: 700;
      cursor: pointer;
    }
    .pincode-result-msg {
      font-size: 0.75rem;
      margin-top: 8px;
      color: #86efac;
      display: none;
    }

    /* Coupon in Drawer */
    .coupon-drawer-row {
      display: flex;
      gap: 8px;
      margin-bottom: 1rem;
    }
    .coupon-drawer-input {
      flex: 1;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 6px;
      padding: 8px 12px;
      color: #fff;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      outline: none;
    }
    .coupon-apply-btn {
      background: rgba(212, 175, 112, 0.15);
      border: 1px solid var(--gold);
      color: var(--gold-light);
      border-radius: 6px;
      padding: 8px 14px;
      font-size: 0.78rem;
      font-weight: 700;
      cursor: pointer;
      transition: var(--trans-smooth);
    }
    .coupon-apply-btn:hover {
      background: var(--gold);
      color: #000;
    }
    .free-sample-picker-wrap {
      background: rgba(212, 175, 112, 0.06);
      border: 1px solid rgba(212, 175, 112, 0.2);
      border-radius: 8px;
      padding: 10px 12px;
      margin-bottom: 1.2rem;
    }
    .free-sample-title {
      font-size: 0.75rem;
      color: var(--gold);
      font-weight: 700;
      margin-bottom: 6px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .free-sample-select {
      width: 100%;
      background: #111;
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #fff;
      padding: 6px 10px;
      border-radius: 6px;
      font-size: 0.78rem;
      outline: none;
    }

    /* ==========================================================
       SIDE-BY-SIDE FRAGRANCE COMPARISON STYLES
       ========================================================== */
    .card-action-btns {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .compare-toggle-btn {
      background: rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1px solid var(--glass-border);
      color: rgba(255, 255, 255, 0.82);
      font-family: var(--nav-font);
      font-size: 0.68rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 5px 10px;
      border-radius: 100px;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      cursor: pointer;
      transition: var(--trans-smooth);
    }
    .compare-toggle-btn:hover {
      border-color: var(--gold);
      color: var(--gold-light);
      background: rgba(212, 175, 112, 0.15);
      transform: translateY(-1px);
    }
    .compare-toggle-btn.active {
      background: var(--gold);
      color: #070707;
      border-color: var(--gold);
      font-weight: 700;
      box-shadow: 0 0 14px rgba(212, 175, 112, 0.5);
    }

    /* Catalog Compare Banner */
    .catalog-compare-banner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
      background: linear-gradient(90deg, rgba(212, 175, 112, 0.12) 0%, rgba(255, 255, 255, 0.03) 100%);
      border: 1px solid rgba(212, 175, 112, 0.25);
      border-radius: 14px;
      padding: 14px 22px;
      margin-bottom: 2.2rem;
      flex-wrap: wrap;
    }
    .compare-banner-left {
      display: flex;
      align-items: center;
      gap: 14px;
      color: rgba(255, 255, 255, 0.85);
      font-size: 0.88rem;
    }
    .compare-icon-badge {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: rgba(212, 175, 112, 0.18);
      border: 1px solid var(--gold);
      color: var(--gold-light);
      font-size: 1.05rem;
      flex-shrink: 0;
    }
    .compare-banner-btn {
      background: rgba(212, 175, 112, 0.18);
      border: 1px solid var(--gold);
      color: var(--gold-light);
      font-family: var(--nav-font);
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 9px 20px;
      border-radius: 100px;
      cursor: pointer;
      transition: var(--trans-smooth);
      white-space: nowrap;
    }
    .compare-banner-btn:hover {
      background: var(--gold);
      color: #070707;
      box-shadow: 0 0 16px rgba(212, 175, 112, 0.4);
    }

    /* Floating Compare Dock / Tray */
    .floating-compare-tray {
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(140%);
      z-index: 1500;
      background: rgba(10, 10, 10, 0.95);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid rgba(212, 175, 112, 0.45);
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.85), 0 0 35px rgba(212, 175, 112, 0.2);
      border-radius: 100px;
      padding: 10px 18px 10px 22px;
      display: flex;
      align-items: center;
      gap: 18px;
      transition: transform 0.45s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.4s ease;
      max-width: 92vw;
      opacity: 0;
      pointer-events: none;
    }
    .floating-compare-tray.visible {
      transform: translateX(-50%) translateY(0);
      opacity: 1;
      pointer-events: auto;
    }
    .compare-tray-left {
      display: flex;
      flex-direction: column;
    }
    .compare-tray-title {
      font-family: var(--nav-font);
      font-size: 0.76rem;
      font-weight: 700;
      letter-spacing: 0.12em;
      color: var(--gold-light);
      text-transform: uppercase;
      white-space: nowrap;
    }
    .compare-tray-subtext {
      font-size: 0.68rem;
      color: var(--muted-color);
      white-space: nowrap;
    }
    .compare-tray-slots {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .compare-slot {
      background: rgba(255, 255, 255, 0.05);
      border: 1px dashed rgba(255, 255, 255, 0.2);
      border-radius: 100px;
      padding: 4px 12px 4px 6px;
      display: flex;
      align-items: center;
      gap: 8px;
      min-width: 145px;
      transition: var(--trans-smooth);
    }
    .compare-slot.filled {
      border-style: solid;
      border-color: rgba(212, 175, 112, 0.4);
      background: rgba(212, 175, 112, 0.1);
    }
    .compare-slot-thumb {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      object-fit: cover;
      background: #111;
      border: 1px solid var(--gold);
    }
    .compare-slot-info {
      display: flex;
      flex-direction: column;
      line-height: 1.2;
    }
    .compare-slot-name {
      font-size: 0.74rem;
      color: #fff;
      font-weight: 600;
      white-space: nowrap;
      max-width: 90px;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .compare-slot-conc {
      font-size: 0.62rem;
      color: var(--gold);
      white-space: nowrap;
    }
    .compare-slot-remove {
      background: none;
      border: none;
      color: rgba(255, 255, 255, 0.45);
      cursor: pointer;
      font-size: 0.85rem;
      padding: 2px 4px;
      transition: color 0.2s;
    }
    .compare-slot-remove:hover {
      color: #ef4444;
    }
    .compare-slot-placeholder {
      font-size: 0.72rem;
      color: rgba(255, 255, 255, 0.45);
      font-style: italic;
      padding: 6px 12px;
      white-space: nowrap;
    }
    .compare-tray-vs {
      font-family: var(--nav-font);
      font-size: 0.68rem;
      font-weight: 800;
      color: var(--gold);
      padding: 3px 7px;
      border-radius: 50%;
      background: rgba(212, 175, 112, 0.15);
      border: 1px solid rgba(212, 175, 112, 0.3);
    }
    .compare-tray-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .compare-tray-btn.primary {
      background: var(--gold);
      color: #070707;
      border: none;
      font-family: var(--nav-font);
      font-size: 0.76rem;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      padding: 9px 18px;
      border-radius: 100px;
      cursor: pointer;
      transition: var(--trans-smooth);
      white-space: nowrap;
      box-shadow: 0 4px 15px rgba(212, 175, 112, 0.35);
    }
    .compare-tray-btn.primary:hover {
      background: var(--gold-light);
      transform: translateY(-2px);
      box-shadow: 0 8px 25px rgba(212, 175, 112, 0.5);
    }
    .compare-tray-btn.clear {
      background: none;
      border: 1px solid rgba(255, 255, 255, 0.18);
      color: rgba(255, 255, 255, 0.65);
      font-size: 0.72rem;
      padding: 7px 12px;
      border-radius: 100px;
      cursor: pointer;
      transition: var(--trans-smooth);
    }
    .compare-tray-btn.clear:hover {
      color: #fff;
      border-color: rgba(255, 255, 255, 0.4);
    }

    /* Side-by-Side Comparison Modal Backdrop & Card */
    .compare-modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(4, 4, 4, 0.92);
      backdrop-filter: blur(28px);
      -webkit-backdrop-filter: blur(28px);
      z-index: 2100;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.4s ease;
    }
    .compare-modal-backdrop.active {
      opacity: 1;
      pointer-events: auto;
    }
    .compare-modal-card {
      background: #090909;
      border: 1px solid rgba(212, 175, 112, 0.35);
      border-radius: 28px;
      max-width: 1200px;
      width: 100%;
      max-height: 92vh;
      overflow-y: auto;
      position: relative;
      box-shadow: 0 40px 100px rgba(0, 0, 0, 0.9), 0 0 50px rgba(212, 175, 112, 0.12);
      transform: scale(0.94);
      transition: transform 0.45s cubic-bezier(0.16, 1, 0.3, 1);
      padding: 3rem 2.5rem;
    }
    .compare-modal-backdrop.active .compare-modal-card {
      transform: scale(1);
    }
    .compare-modal-header {
      text-align: center;
      margin-bottom: 2rem;
    }
    .compare-modal-title {
      font-family: var(--heading-font);
      font-size: 2.3rem;
      color: #fff;
      margin: 6px 0 8px 0;
    }
    .compare-modal-subtitle {
      font-size: 0.9rem;
      color: var(--muted-color);
      max-width: 680px;
      margin: 0 auto;
      line-height: 1.6;
    }

    /* Dynamic Dropdown Selectors inside Modal */
    .compare-select-bar {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 1.5rem;
      background: rgba(255, 255, 255, 0.035);
      border: 1px solid var(--glass-border);
      border-radius: 16px;
      padding: 1rem 1.5rem;
      margin-bottom: 2.5rem;
      flex-wrap: wrap;
    }
    .compare-select-wrapper {
      display: flex;
      align-items: center;
      gap: 10px;
      flex: 1;
      min-width: 260px;
    }
    .compare-select-label {
      font-family: var(--nav-font);
      font-size: 0.75rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--gold);
      white-space: nowrap;
      font-weight: 700;
    }
    .compare-perfume-select {
      flex: 1;
      background: #111;
      border: 1px solid rgba(212, 175, 112, 0.3);
      color: #fff;
      font-size: 0.85rem;
      padding: 10px 16px;
      border-radius: 10px;
      outline: none;
      cursor: pointer;
    }
    .compare-swap-btn {
      background: rgba(212, 175, 112, 0.15);
      border: 1px solid var(--gold);
      color: var(--gold-light);
      border-radius: 100px;
      padding: 8px 16px;
      font-family: var(--nav-font);
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
      transition: var(--trans-smooth);
    }
    .compare-swap-btn:hover {
      background: var(--gold);
      color: #000;
    }

    /* Comparison Columns & Table */
    .compare-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2.5rem;
      position: relative;
    }
    .compare-grid::after {
      content: 'VS';
      position: absolute;
      top: 130px;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: #161616;
      border: 2px solid var(--gold);
      color: var(--gold);
      font-family: var(--nav-font);
      font-size: 0.85rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 25px rgba(212, 175, 112, 0.4);
      z-index: 5;
    }
    .compare-column {
      background: rgba(255, 255, 255, 0.025);
      border: 1px solid var(--glass-border);
      border-radius: 20px;
      padding: 2rem;
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      transition: border-color 0.3s ease;
    }
    .compare-column:hover {
      border-color: rgba(212, 175, 112, 0.4);
    }
    .compare-flacon-stage {
      width: 100%;
      height: 240px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: radial-gradient(circle, rgba(255, 255, 255, 0.06) 0%, transparent 70%);
      border-radius: 14px;
      position: relative;
      overflow: hidden;
    }
    .compare-flacon-img {
      max-height: 85%;
      max-width: 85%;
      object-fit: contain;
      filter: drop-shadow(0 15px 25px rgba(0, 0, 0, 0.7));
      transition: transform 0.5s ease;
    }
    .compare-column:hover .compare-flacon-img {
      transform: scale(1.06);
    }
    .compare-brand-tag {
      font-family: var(--nav-font);
      font-size: 0.72rem;
      letter-spacing: 0.25em;
      text-transform: uppercase;
      color: var(--gold);
    }
    .compare-prod-name {
      font-family: var(--heading-font);
      font-size: 1.8rem;
      color: #fff;
      margin: 4px 0 6px 0;
    }
    .compare-family-badge {
      display: inline-block;
      font-family: var(--nav-font);
      font-size: 0.65rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      padding: 3px 10px;
      border-radius: 100px;
      background: rgba(212, 175, 112, 0.15);
      border: 1px solid rgba(212, 175, 112, 0.3);
      color: var(--gold-light);
      margin-bottom: 8px;
    }

    /* Comparison Metric Cards */
    .compare-metric-box {
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 14px;
      padding: 1.25rem;
    }
    .compare-metric-title {
      font-family: var(--nav-font);
      font-size: 0.72rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--gold);
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .compare-price-val {
      font-size: 1.6rem;
      font-weight: 700;
      color: #fff;
      font-family: var(--nav-font);
    }
    .compare-price-delta {
      display: inline-block;
      font-size: 0.72rem;
      padding: 2px 8px;
      border-radius: 100px;
      margin-left: 8px;
    }
    .compare-price-delta.cheaper {
      background: rgba(74, 222, 128, 0.15);
      color: #4ade80;
      border: 1px solid rgba(74, 222, 128, 0.3);
    }
    .compare-price-delta.higher {
      background: rgba(212, 175, 112, 0.15);
      color: var(--gold-light);
      border: 1px solid rgba(212, 175, 112, 0.3);
    }
    .compare-unit-price {
      font-size: 0.75rem;
      color: var(--muted-color);
      margin-top: 2px;
    }

    /* Sillage & Longevity Bar */
    .compare-bar-track {
      width: 100%;
      height: 8px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 100px;
      margin: 8px 0 6px 0;
      overflow: hidden;
    }
    .compare-bar-fill {
      height: 100%;
      background: linear-gradient(90deg, #d4af70 0%, #fbcfe8 100%);
      border-radius: 100px;
      transition: width 0.6s ease;
    }
    .compare-bar-meta {
      display: flex;
      justify-content: space-between;
      font-size: 0.72rem;
      color: var(--muted-color);
    }

    /* Olfactory Notes comparison block */
    .compare-notes-tier {
      margin-bottom: 0.85rem;
    }
    .compare-notes-tier:last-child {
      margin-bottom: 0;
    }
    .compare-tier-heading {
      font-size: 0.68rem;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--gold-light);
      margin-bottom: 4px;
      font-family: var(--nav-font);
    }
    .compare-notes-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 5px;
    }
    .note-pill-tag {
      font-size: 0.72rem;
      padding: 3px 8px;
      border-radius: 6px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: rgba(255, 255, 255, 0.85);
    }
    .note-pill-tag.shared {
      background: rgba(212, 175, 112, 0.22);
      border-color: var(--gold);
      color: var(--gold-light);
      font-weight: 600;
      box-shadow: 0 0 8px rgba(212, 175, 112, 0.35);
    }

    /* Shared Accords Banner across both columns */
    .compare-shared-accords-box {
      grid-column: 1 / -1;
      background: linear-gradient(90deg, rgba(212, 175, 112, 0.12) 0%, rgba(251, 207, 232, 0.08) 100%);
      border: 1px solid rgba(212, 175, 112, 0.3);
      border-radius: 16px;
      padding: 1.25rem 1.75rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
      flex-wrap: wrap;
    }
    .shared-accords-title {
      font-family: var(--nav-font);
      font-size: 0.75rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--gold);
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .shared-accords-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }

    /* Compare Action Buttons */
    .compare-actions-col {
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-top: auto;
    }
    .compare-add-btn {
      width: 100%;
      background: var(--gold);
      color: #070707;
      border: none;
      font-family: var(--nav-font);
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      padding: 12px;
      border-radius: 100px;
      cursor: pointer;
      transition: var(--trans-smooth);
    }
    .compare-add-btn:hover {
      background: var(--gold-light);
      transform: translateY(-2px);
      box-shadow: 0 8px 25px rgba(212, 175, 112, 0.4);
    }
    .compare-engrave-btn {
      width: 100%;
      background: transparent;
      border: 1px solid rgba(212, 175, 112, 0.4);
      color: var(--gold-light);
      font-family: var(--nav-font);
      font-size: 0.74rem;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 10px;
      border-radius: 100px;
      cursor: pointer;
      transition: var(--trans-smooth);
    }
    .compare-engrave-btn:hover {
      background: rgba(212, 175, 112, 0.15);
      border-color: var(--gold);
      color: #fff;
    }

    .modal-compare-action-btn {
      width: 100%;
      background: rgba(212, 175, 112, 0.1);
      border: 1px solid rgba(212, 175, 112, 0.35);
      color: var(--gold-light);
      font-family: var(--nav-font);
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      padding: 12px;
      border-radius: 100px;
      cursor: pointer;
      transition: var(--trans-smooth);
      margin-top: 10px;
    }
    .modal-compare-action-btn:hover {
      background: var(--gold);
      color: #070707;
      border-color: var(--gold);
      box-shadow: 0 6px 20px rgba(212, 175, 112, 0.3);
    }

    /* Media queries for new sections */
    @media (max-width: 1024px) {
      .myop-studio-grid,
      .personalise-studio-card,
      .corporate-grid,
      .refill-card-wrap {
        grid-template-columns: 1fr;
      }
      .flacon-visualizer-sticky {
        position: static;
        margin-top: 2rem;
      }
      .discovery-sets-grid,
      .deals-grid,
      .stores-cards-grid {
        grid-template-columns: repeat(2, 1fr);
      }
      .compare-grid {
        grid-template-columns: 1fr;
        gap: 2rem;
      }
      .compare-grid::after {
        display: none;
      }
    }
    @media (max-width: 768px) {
      .top-announcement-bar {
        display: none;
      }
      .flacon-picker-grid,
      .discovery-sets-grid,
      .deals-grid,
      .stores-cards-grid {
        grid-template-columns: 1fr;
      }
      .personalise-studio-card {
        padding: 2rem 1.25rem;
      }
      .myop-hero-banner {
        flex-direction: column;
        text-align: center;
        padding: 2rem 1.5rem;
      }
      .floating-compare-tray {
        flex-direction: column;
        border-radius: 20px;
        padding: 14px 18px;
        bottom: 12px;
        width: 95vw;
        gap: 12px;
      }
      .compare-tray-slots {
        width: 100%;
        justify-content: space-between;
      }
      .compare-slot {
        min-width: 0;
        flex: 1;
      }
      .compare-tray-actions {
        width: 100%;
        justify-content: space-between;
      }
      .compare-tray-btn.primary {
        flex: 1;
        text-align: center;
      }
      .compare-modal-card {
        padding: 2.2rem 1.2rem;
      }
    }

    /* Accessibility / Reduced Motion */
    @media (prefers-reduced-motion: reduce) {
      * {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }
    }

    /* =====================================================
       TRACK ORDER MODAL
       ===================================================== */
    .track-order-modal-backdrop {
      position: fixed;
      inset: 0;
      z-index: 2000;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1rem;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.35s ease;
    }
    .track-order-modal-backdrop.active {
      opacity: 1;
      pointer-events: all;
    }
    .track-order-card {
      background: linear-gradient(145deg, #0f0f0f 0%, #141414 100%);
      border: 1px solid rgba(212, 175, 112, 0.22);
      border-radius: 20px;
      width: 100%;
      max-width: 560px;
      padding: 2.5rem;
      position: relative;
      box-shadow: 0 40px 100px rgba(0, 0, 0, 0.85);
      transform: translateY(18px) scale(0.97);
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      max-height: 90vh;
      overflow-y: auto;
    }
    .track-order-modal-backdrop.active .track-order-card {
      transform: translateY(0) scale(1);
    }
    .track-info-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      background: rgba(212, 175, 112, 0.06);
      border: 1px solid rgba(212, 175, 112, 0.14);
      border-radius: 12px;
      padding: 1rem 1.2rem;
      margin-bottom: 1.5rem;
    }
    .track-timeline {
      display: flex;
      flex-direction: column;
      gap: 0;
      position: relative;
    }
    .track-timeline::before {
      content: "";
      position: absolute;
      left: 14px;
      top: 16px;
      bottom: 16px;
      width: 2px;
      background: rgba(212, 175, 112, 0.15);
    }
    .timeline-node {
      display: flex;
      gap: 1rem;
      align-items: flex-start;
      padding: 0.9rem 0;
      position: relative;
    }
    .timeline-dot {
      width: 30px;
      height: 30px;
      border-radius: 50%;
      flex-shrink: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.8rem;
      font-weight: 700;
      background: rgba(255, 255, 255, 0.05);
      border: 2px solid rgba(255, 255, 255, 0.12);
      color: var(--muted-color);
      position: relative;
      z-index: 1;
    }
    .timeline-node.complete .timeline-dot {
      background: linear-gradient(135deg, var(--gold) 0%, #b8860b 100%);
      border-color: var(--gold);
      color: #000;
      box-shadow: 0 0 12px rgba(212, 175, 112, 0.35);
    }
    .timeline-node.active .timeline-dot {
      background: rgba(212, 175, 112, 0.1);
      border-color: var(--gold);
      color: var(--gold);
      box-shadow: 0 0 16px rgba(212, 175, 112, 0.3);
      animation: trackPulse 1.5s ease-in-out infinite;
    }
    @keyframes trackPulse {
      0%, 100% { box-shadow: 0 0 8px rgba(212, 175, 112, 0.25); }
      50% { box-shadow: 0 0 20px rgba(212, 175, 112, 0.55); }
    }
    .timeline-info h4 {
      font-size: 0.88rem;
      font-weight: 600;
      color: #fff;
      margin-bottom: 3px;
    }
    .timeline-info p {
      font-size: 0.75rem;
      color: var(--muted-color);
      line-height: 1.5;
      margin-bottom: 4px;
    }
    .timeline-time {
      font-size: 0.7rem;
      color: var(--gold);
      font-family: var(--nav-font);
    }
    .timeline-node.active .timeline-info h4 {
      color: var(--gold);
    }

    /* =====================================================
       BOOK STORE APPOINTMENT MODAL
       ===================================================== */
    .book-store-modal-backdrop {
      position: fixed;
      inset: 0;
      z-index: 2100;
      background: rgba(0, 0, 0, 0.88);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1rem;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.35s ease;
    }
    .book-store-modal-backdrop.active {
      opacity: 1;
      pointer-events: all;
    }
    .book-store-card {
      background: linear-gradient(145deg, #0f0f0f 0%, #141414 100%);
      border: 1px solid rgba(212, 175, 112, 0.22);
      border-radius: 20px;
      width: 100%;
      max-width: 540px;
      padding: 2.5rem;
      position: relative;
      box-shadow: 0 40px 100px rgba(0, 0, 0, 0.85);
      transform: translateY(18px) scale(0.97);
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      max-height: 90vh;
      overflow-y: auto;
    }
    .book-store-modal-backdrop.active .book-store-card {
      transform: translateY(0) scale(1);
    }

    /* =====================================================
       CHECKOUT MODAL SYSTEM
       ===================================================== */
    .checkout-modal-backdrop {
      position: fixed;
      inset: 0;
      z-index: 1100;
      background: rgba(0,0,0,0.88);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      display: flex;
      align-items: flex-start;
      justify-content: center;
      overflow-y: auto;
      padding: 2rem 1rem;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.35s ease;
    }
    .checkout-modal-backdrop.active {
      opacity: 1;
      pointer-events: all;
    }
    .checkout-modal-card {
      background: linear-gradient(145deg, #0f0f0f 0%, #141414 100%);
      border: 1px solid rgba(212,175,112,0.2);
      border-radius: 20px;
      width: 100%;
      max-width: 960px;
      padding: 2.5rem;
      position: relative;
      box-shadow: 0 40px 120px rgba(0,0,0,0.8), 0 0 0 1px rgba(212,175,112,0.08);
      transform: translateY(20px);
      transition: transform 0.35s cubic-bezier(0.16,1,0.3,1);
    }
    .checkout-modal-backdrop.active .checkout-modal-card {
      transform: translateY(0);
    }
    .checkout-modal-close {
      position: absolute;
      top: 1.5rem;
      right: 1.5rem;
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.1);
      color: #fff;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      font-size: 1.2rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.25s ease;
    }
    .checkout-modal-close:hover {
      background: rgba(212,175,112,0.15);
      border-color: var(--gold);
      color: var(--gold);
    }
    .checkout-modal-header {
      text-align: center;
      margin-bottom: 2.5rem;
      padding-bottom: 1.5rem;
      border-bottom: 1px solid rgba(212,175,112,0.12);
    }
    .checkout-modal-header .eyebrow {
      font-family: var(--nav-font);
      font-size: 0.68rem;
      letter-spacing: 0.22em;
      color: var(--gold);
      text-transform: uppercase;
      margin-bottom: 0.5rem;
      display: block;
    }
    .checkout-modal-header h2 {
      font-family: var(--heading-font);
      font-size: clamp(1.5rem, 3vw, 2rem);
      font-weight: 500;
      color: #fff;
    }
    .checkout-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2rem;
    }
    @media (max-width: 700px) {
      .checkout-grid { grid-template-columns: 1fr; }
      .checkout-modal-card { padding: 1.5rem 1rem; }
    }
    .checkout-section-title {
      font-family: var(--nav-font);
      font-size: 0.72rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--gold);
      margin-bottom: 1.2rem;
      padding-bottom: 0.6rem;
      border-bottom: 1px solid rgba(212,175,112,0.12);
    }
    .checkout-field {
      margin-bottom: 1.1rem;
    }
    .checkout-field label {
      display: block;
      font-size: 0.75rem;
      color: var(--muted-color);
      margin-bottom: 0.45rem;
      font-family: var(--nav-font);
      letter-spacing: 0.05em;
    }
    .checkout-input {
      width: 100%;
      background: rgba(255,255,255,0.04);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 10px;
      color: #fff;
      font-family: var(--body-font);
      font-size: 0.9rem;
      padding: 0.7rem 1rem;
      transition: border-color 0.25s ease, background 0.25s ease;
      outline: none;
    }
    .checkout-input:focus {
      border-color: rgba(212,175,112,0.5);
      background: rgba(212,175,112,0.04);
      box-shadow: 0 0 0 3px rgba(212,175,112,0.08);
    }
    .checkout-input::placeholder { color: rgba(255,255,255,0.3); }

    /* Order Summary Box */
    .order-summary-box {
      background: rgba(212,175,112,0.04);
      border: 1px solid rgba(212,175,112,0.12);
      border-radius: 14px;
      padding: 1.4rem;
    }
    .order-item-row {
      display: flex;
      align-items: center;
      gap: 0.8rem;
      padding: 0.7rem 0;
      border-bottom: 1px solid rgba(255,255,255,0.06);
    }
    .order-item-row:last-of-type { border-bottom: none; }
    .order-item-thumb {
      width: 44px;
      height: 54px;
      object-fit: cover;
      border-radius: 8px;
      border: 1px solid rgba(255,255,255,0.08);
      flex-shrink: 0;
    }
    .order-item-info { flex: 1; min-width: 0; }
    .order-item-name {
      font-size: 0.85rem;
      font-weight: 600;
      color: #fff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .order-item-meta {
      font-size: 0.72rem;
      color: var(--muted-color);
    }
    .order-item-price {
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--gold);
      flex-shrink: 0;
    }
    .order-totals {
      margin-top: 1rem;
      padding-top: 1rem;
      border-top: 1px solid rgba(212,175,112,0.15);
    }
    .order-total-row {
      display: flex;
      justify-content: space-between;
      font-size: 0.82rem;
      color: var(--muted-color);
      margin-bottom: 0.5rem;
    }
    .order-total-row.grand {
      font-size: 1.05rem;
      font-weight: 700;
      color: #fff;
      margin-top: 0.6rem;
      padding-top: 0.6rem;
      border-top: 1px solid rgba(255,255,255,0.1);
    }
    .order-total-row.grand span:last-child { color: var(--gold); }
    .checkout-proceed-btn {
      width: 100%;
      margin-top: 2rem;
      padding: 1rem 2rem;
      background: linear-gradient(135deg, var(--gold) 0%, #b8860b 100%);
      color: #000;
      font-family: var(--nav-font);
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      border: none;
      border-radius: 12px;
      cursor: pointer;
      transition: all 0.3s ease;
      box-shadow: 0 6px 30px rgba(212,175,112,0.25);
    }
    .checkout-proceed-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 12px 40px rgba(212,175,112,0.4);
    }
    .checkout-proceed-btn:disabled {
      opacity: 0.5;
      cursor: not-allowed;
      transform: none;
    }
    .field-error {
      font-size: 0.72rem;
      color: #f87171;
      margin-top: 0.3rem;
      display: none;
    }
    .checkout-input.error { border-color: #f87171; }

    /* =====================================================
       PAYMENT MODAL
       ===================================================== */
    .payment-modal-backdrop {
      position: fixed;
      inset: 0;
      z-index: 1200;
      background: rgba(0,0,0,0.92);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1rem;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease;
    }
    .payment-modal-backdrop.active {
      opacity: 1;
      pointer-events: all;
    }
    .payment-modal-card {
      background: linear-gradient(145deg, #0f0f0f 0%, #141414 100%);
      border: 1px solid rgba(212,175,112,0.25);
      border-radius: 20px;
      width: 100%;
      max-width: 520px;
      padding: 2.5rem;
      position: relative;
      box-shadow: 0 40px 120px rgba(0,0,0,0.9);
      transform: scale(0.95);
      transition: transform 0.3s cubic-bezier(0.16,1,0.3,1);
    }
    .payment-modal-backdrop.active .payment-modal-card {
      transform: scale(1);
    }
    .payment-modal-close {
      position: absolute;
      top: 1.2rem;
      right: 1.2rem;
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.1);
      color: #fff;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      font-size: 1rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .payment-modal-title {
      font-family: var(--heading-font);
      font-size: 1.5rem;
      color: #fff;
      margin-bottom: 0.4rem;
    }
    .payment-modal-subtitle {
      font-size: 0.82rem;
      color: var(--muted-color);
      margin-bottom: 1.8rem;
    }
    .payment-amount-badge {
      background: rgba(212,175,112,0.1);
      border: 1px solid rgba(212,175,112,0.2);
      border-radius: 10px;
      padding: 0.8rem 1.2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.8rem;
    }
    .payment-amount-badge .label {
      font-size: 0.75rem;
      color: var(--muted-color);
      font-family: var(--nav-font);
    }
    .payment-amount-badge .amount {
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--gold);
      font-family: var(--heading-font);
    }
    .payment-methods-label {
      font-family: var(--nav-font);
      font-size: 0.7rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--muted-color);
      margin-bottom: 1rem;
    }
    .payment-method-options {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      margin-bottom: 1.8rem;
    }
    .payment-method-option {
      display: flex;
      align-items: center;
      gap: 1rem;
      padding: 1rem 1.2rem;
      background: rgba(255,255,255,0.03);
      border: 1.5px solid rgba(255,255,255,0.08);
      border-radius: 12px;
      cursor: pointer;
      transition: all 0.25s ease;
      position: relative;
    }
    .payment-method-option:hover {
      border-color: rgba(212,175,112,0.3);
      background: rgba(212,175,112,0.04);
    }
    .payment-method-option.selected {
      border-color: var(--gold);
      background: rgba(212,175,112,0.08);
    }
    .payment-method-option input[type="radio"] {
      accent-color: var(--gold);
      width: 16px;
      height: 16px;
      flex-shrink: 0;
    }
    .payment-method-icon {
      font-size: 1.4rem;
      flex-shrink: 0;
    }
    .payment-method-info { flex: 1; }
    .payment-method-name {
      font-size: 0.9rem;
      font-weight: 600;
      color: #fff;
      display: block;
    }
    .payment-method-desc {
      font-size: 0.72rem;
      color: var(--muted-color);
    }
    .payment-upi-field {
      margin-bottom: 1.2rem;
      display: none;
    }
    .payment-upi-field.visible { display: block; }
    .payment-card-fields {
      display: none;
      gap: 0.8rem;
      flex-direction: column;
      margin-bottom: 1.2rem;
    }
    .payment-card-fields.visible { display: flex; }
    .payment-card-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.8rem;
    }
    .pay-now-btn {
      width: 100%;
      padding: 1rem 2rem;
      background: linear-gradient(135deg, var(--gold) 0%, #b8860b 100%);
      color: #000;
      font-family: var(--nav-font);
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      border: none;
      border-radius: 12px;
      cursor: pointer;
      transition: all 0.3s ease;
      box-shadow: 0 6px 30px rgba(212,175,112,0.3);
    }
    .pay-now-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 12px 40px rgba(212,175,112,0.45);
    }
    .payment-secure-notice {
      text-align: center;
      font-size: 0.68rem;
      color: rgba(255,255,255,0.35);
      margin-top: 1rem;
    }
    .payment-secure-notice span { margin: 0 0.4rem; }

    /* =====================================================
       ORDER SUCCESS MODAL
       ===================================================== */
    .order-success-backdrop {
      position: fixed;
      inset: 0;
      z-index: 1300;
      background: rgba(0,0,0,0.95);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1rem;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.4s ease;
    }
    .order-success-backdrop.active {
      opacity: 1;
      pointer-events: all;
    }
    .order-success-card {
      background: linear-gradient(145deg, #0f0f0f 0%, #141414 100%);
      border: 1px solid rgba(212,175,112,0.25);
      border-radius: 24px;
      width: 100%;
      max-width: 480px;
      padding: 3rem 2.5rem;
      text-align: center;
      position: relative;
      box-shadow: 0 40px 120px rgba(0,0,0,0.9), 0 0 60px rgba(212,175,112,0.06);
      transform: scale(0.9);
      transition: transform 0.4s cubic-bezier(0.16,1,0.3,1);
    }
    .order-success-backdrop.active .order-success-card {
      transform: scale(1);
    }
    .success-checkmark {
      width: 72px;
      height: 72px;
      background: linear-gradient(135deg, var(--gold) 0%, #b8860b 100%);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 1.5rem;
      font-size: 2rem;
      box-shadow: 0 0 40px rgba(212,175,112,0.3);
      animation: successPulse 0.6s ease forwards;
    }
    @keyframes successPulse {
      0% { transform: scale(0.5); opacity: 0; }
      70% { transform: scale(1.12); }
      100% { transform: scale(1); opacity: 1; }
    }
    .success-title {
      font-family: var(--heading-font);
      font-size: 1.8rem;
      color: #fff;
      margin-bottom: 0.5rem;
    }
    .success-subtitle {
      font-size: 0.85rem;
      color: var(--muted-color);
      margin-bottom: 2rem;
      line-height: 1.6;
    }
    .success-order-id {
      background: rgba(212,175,112,0.08);
      border: 1px solid rgba(212,175,112,0.2);
      border-radius: 10px;
      padding: 0.8rem 1.4rem;
      margin-bottom: 1.8rem;
    }
    .success-order-id .label {
      font-size: 0.7rem;
      color: var(--muted-color);
      text-transform: uppercase;
      letter-spacing: 0.1em;
    }
    .success-order-id .id {
      font-size: 1rem;
      font-weight: 700;
      color: var(--gold);
      font-family: var(--nav-font);
      letter-spacing: 0.08em;
    }
    .success-close-btn {
      width: 100%;
      padding: 0.9rem;
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.12);
      border-radius: 12px;
      color: #fff;
      font-family: var(--nav-font);
      font-size: 0.8rem;
      letter-spacing: 0.1em;
      cursor: pointer;
      transition: all 0.25s ease;
    }
    .success-close-btn:hover {
      background: rgba(212,175,112,0.1);
      border-color: var(--gold);
      color: var(--gold);
    }

    /* Payment loading spinner */
    .pay-spinner {
      display: inline-block;
      width: 16px;
      height: 16px;
      border: 2px solid rgba(0,0,0,0.3);
      border-top-color: #000;
      border-radius: 50%;
      animation: spin 0.7s linear infinite;
      margin-right: 8px;
      vertical-align: middle;
    }
    @keyframes spin { to { transform: rotate(360deg); } }

  
    /* ==========================================================
       ADMIN PORTAL & ORDER MANAGEMENT STYLES
       ========================================================== */
    .admin-portal-view {
      position: fixed;
      inset: 0;
      z-index: 5000;
      background: #080808;
      color: var(--cream);
      display: none;
      flex-direction: column;
      overflow-y: auto;
      font-family: var(--font-body);
    }
    .admin-portal-view.active {
      display: flex;
    }
    .admin-top-bar {
      background: rgba(15, 15, 15, 0.95);
      border-bottom: 1px solid rgba(212, 175, 112, 0.25);
      padding: 1rem 2rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 10;
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
    }
    .admin-brand-wrap {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .admin-brand-tag {
      font-family: var(--heading-font);
      font-size: 1.25rem;
      letter-spacing: 0.15em;
      color: var(--gold-light);
    }
    .admin-badge-atelier {
      background: rgba(212, 175, 112, 0.15);
      border: 1px solid rgba(212, 175, 112, 0.35);
      color: var(--gold);
      font-size: 0.65rem;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      padding: 3px 8px;
      border-radius: 999px;
    }
    .admin-actions-wrap {
      display: flex;
      align-items: center;
      gap: 1rem;
    }
    .admin-portal-content {
      max-width: 1300px;
      width: 100%;
      margin: 0 auto;
      padding: 2.5rem 1.5rem 5rem 1.5rem;
    }
    .admin-stats-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1.25rem;
      margin-bottom: 2.5rem;
    }
    .admin-stat-card {
      background: linear-gradient(145deg, #111111 0%, #171717 100%);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 16px;
      padding: 1.4rem 1.6rem;
      display: flex;
      flex-direction: column;
      gap: 6px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }
    .admin-stat-label {
      font-size: 0.72rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--muted-color);
    }
    .admin-stat-val {
      font-family: var(--heading-font);
      font-size: 1.8rem;
      color: #fff;
    }
    .admin-stat-sub {
      font-size: 0.75rem;
      color: var(--gold-light);
    }

    /* Admin Toolbar */
    .admin-toolbar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1rem;
      margin-bottom: 1.5rem;
      background: rgba(20, 20, 20, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.06);
      padding: 1rem 1.25rem;
      border-radius: 14px;
    }
    .admin-filter-tabs {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .admin-filter-btn {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: var(--muted-color);
      padding: 6px 14px;
      border-radius: 999px;
      font-size: 0.75rem;
      cursor: pointer;
      transition: all 0.25s ease;
    }
    .admin-filter-btn:hover {
      color: #fff;
      border-color: rgba(212, 175, 112, 0.4);
    }
    .admin-filter-btn.active {
      background: var(--gold);
      color: #000;
      font-weight: 700;
      border-color: var(--gold);
    }
    .admin-search-wrap {
      display: flex;
      align-items: center;
      gap: 8px;
      min-width: 260px;
    }

    /* Orders Table / Cards */
    .admin-orders-table-wrap {
      background: #111111;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 18px;
      overflow: hidden;
      box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6);
    }
    .admin-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.82rem;
      text-align: left;
    }
    .admin-table th {
      background: rgba(255, 255, 255, 0.03);
      padding: 1rem 1.2rem;
      font-size: 0.72rem;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--muted-color);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }
    .admin-table td {
      padding: 1.1rem 1.2rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
      vertical-align: middle;
    }
    .admin-table tr:hover td {
      background: rgba(212, 175, 112, 0.03);
    }
    .order-status-badge {
      display: inline-block;
      padding: 4px 10px;
      border-radius: 999px;
      font-size: 0.7rem;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
    }
    .badge-placed {
      background: rgba(212, 175, 112, 0.15);
      color: var(--gold-light);
      border: 1px solid rgba(212, 175, 112, 0.3);
    }
    .badge-processing {
      background: rgba(59, 130, 246, 0.15);
      color: #60a5fa;
      border: 1px solid rgba(59, 130, 246, 0.3);
    }
    .badge-shipped {
      background: rgba(168, 85, 247, 0.15);
      color: #c084fc;
      border: 1px solid rgba(168, 85, 247, 0.3);
    }
    .badge-delivered {
      background: rgba(34, 197, 94, 0.15);
      color: #4ade80;
      border: 1px solid rgba(34, 197, 94, 0.3);
    }
    .badge-cancelled {
      background: rgba(239, 68, 68, 0.15);
      color: #f87171;
      border: 1px solid rgba(239, 68, 68, 0.3);
    }

    .admin-status-select {
      background: #191919;
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #fff;
      padding: 5px 10px;
      border-radius: 8px;
      font-size: 0.76rem;
      cursor: pointer;
      outline: none;
      transition: border-color 0.2s;
    }
    .admin-status-select:focus {
      border-color: var(--gold);
    }

    /* Admin Login Modal */
    .admin-login-modal-backdrop {
      position: fixed;
      inset: 0;
      z-index: 6000;
      background: rgba(0, 0, 0, 0.88);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1rem;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.35s ease;
    }
    .admin-login-modal-backdrop.active {
      opacity: 1;
      pointer-events: all;
    }
    .admin-login-card {
      background: linear-gradient(145deg, #111 0%, #181818 100%);
      border: 1px solid rgba(212, 175, 112, 0.3);
      border-radius: 20px;
      width: 100%;
      max-width: 400px;
      padding: 2.5rem;
      text-align: center;
      box-shadow: 0 40px 100px rgba(0, 0, 0, 0.9);
      position: relative;
    }
    .admin-pin-input {
      letter-spacing: 0.4em;
      font-size: 1.5rem;
      text-align: center;
      background: #090909;
      border: 1px solid rgba(212, 175, 112, 0.35);
      border-radius: 12px;
      color: var(--gold-light);
      padding: 12px;
      width: 100%;
      margin: 1.5rem 0;
      outline: none;
    }
    .admin-pin-input:focus {
      border-color: var(--gold);
      box-shadow: 0 0 16px rgba(212, 175, 112, 0.25);
    }

    @media (max-width: 768px) {
      .admin-top-bar {
        padding: 0.85rem 1rem;
      }
      .admin-portal-content {
        padding: 1.5rem 1rem 4rem 1rem;
      }
      .admin-toolbar {
        flex-direction: column;
        align-items: stretch;
      }
      .admin-table th, .admin-table td {
        padding: 0.8rem 0.6rem;
        font-size: 0.75rem;
      }
    }
  </style>
</head>
"""
