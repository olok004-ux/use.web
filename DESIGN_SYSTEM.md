# DESIGN SYSTEM (Tokens)

## CSS Variables from :root

```css
/* ============================================================
① DESIGN SYSTEM 공식 토큰 (DESIGN.md 기준 — 원본 헥스값)
============================================================ */
/* Gray */
--color-gray-50:  #f7f9fc;
--color-gray-100: #dce3ec;
--color-gray-200: #c4cdd9;
--color-gray-300: #98a2b3;
--color-gray-400: #667085;
--color-gray-500: #475467;
--color-gray-600: #344054;
--color-gray-700: #1d2939;
/* Blue — Brand Primary */
--color-blue-50:  #e7f0ff;
--color-blue-100: #dce8ff;
--color-blue-200: #c2d9ff;
--color-blue-300: #9ec3ff;
--color-blue-400: #6fa6ff;
--color-blue-500: #126dfb;
--color-blue-600: #0f5fe0;
--color-blue-700: #0c4fc2;
--color-blue-800: #093fa3;
--color-blue-900: #003486;
/* Blue Secondary (Material) */
--color-blue-secondary-50:  #e3f2fd;
--color-blue-secondary-100: #bbdefb;
--color-blue-secondary-200: #90caf9;
--color-blue-secondary-300: #64b5f6;
--color-blue-secondary-400: #2196f3;
--color-blue-secondary-500: #1e88e5;
--color-blue-secondary-600: #1976d2;
--color-blue-secondary-700: #1565c0;
/* Amber — Warning */
--color-amber-50:  #fff8e1;
--color-amber-100: #ffecb3;
--color-amber-200: #ffe082;
--color-amber-300: #ffd54f;
--color-amber-400: #ffc107;
--color-amber-500: #ffb300;
--color-amber-600: #ffa000;
--color-amber-700: #ff8f00;
--color-amber-800: #ff6f00;
/* Red — Error */
--color-red-50:  #fdecea;
--color-red-100: #f9c1bc;
--color-red-200: #f28b82;
--color-red-300: #e57373;
--color-red-400: #f44336;
--color-red-500: #e53935;
--color-red-600: #d32f2f;
--color-red-700: #c62828;
--color-red-800: #b71c1c;
/* Semantic */
--color-primary:              #1041a7;
--color-primary-variant:      #0f5fe0;
--color-on-primary:           #ffffff;
--color-primary-container:    #dce8ff;
--color-on-primary-container: #003486;
--color-surface:              #fafafa;
--color-navy-title:           #071b44; /* 섹션 타이틀 (Figma 1011-2464) */
/* Typography — Font Size */
--font-size-display-lg:  3rem;
--font-size-display-md:  2.5rem;
--font-size-display-sm:  2rem;
--font-size-headline-lg: 1.75rem;
--font-size-headline-md: 1.5rem;
--font-size-headline-sm: 1.25rem;
--font-size-body:        1rem;
--font-size-label:       0.875rem;
--font-size-caption:     0.75rem;
/* Typography — Font Weight */
--font-weight-heavy:      900;
--font-weight-extra-bold: 800;
--font-weight-bold:       700;
--font-weight-semi-bold:  600;
--font-weight-medium:     500;
--font-weight-regular:    400;
/* Spacing */
--spacing-2:    0.125rem;
--spacing-4:    0.25rem;
--spacing-6:    0.375rem;
--spacing-8:    0.5rem;
--spacing-10:   0.625rem;
--spacing-12:   0.75rem;
--spacing-14:   0.875rem;
--spacing-16:   1rem;
--spacing-20:   1.25rem;
--spacing-24:   1.5rem;
--spacing-32:   2rem;
--spacing-80:   5rem;
--spacing-260:  16.25rem;
--spacing-1000: 62.5rem;
/* Border Radius */
--radius-sm:   0.25rem;
--radius-md:   0.75rem;
--radius-lg:   1rem;
--radius-xl:   1.25rem;
--radius-full: 9999px;
/* Shadow */
--shadow-s: 0px 2px 15px 2px rgba(18,18,18,0.05);
--shadow-m: 0px 3px 13px -3px rgba(18,18,18,0.20);
--shadow-l: 0px 5px 10px -3px rgba(18,18,18,0.20);
/* ============================================================
② 하위 호환 별칭 — 기존 코드가 그대로 동작하도록
(신규 코드 작성 시 위 공식 토큰 사용)
============================================================ */
/* Blue 별칭 */
--primary:      var(--color-blue-500);
--primary-dk:   var(--color-blue-600);
--primary-lt:   var(--color-blue-200);
--main:         var(--color-primary);
--secondary:    var(--color-blue-500);
--secondary-lt: var(--color-blue-200);
--blue-50:      var(--color-blue-50);
--blue-700:     var(--color-blue-700);
--blue-900:     var(--color-blue-900);
/* Red / Amber 별칭 */
--red-400:   var(--color-red-400);
--red-500:   var(--color-red-500);
--red-50:    var(--color-red-50);
--danger:    var(--color-red-600);
--amber-800: var(--color-amber-800);
/* Gray 별칭 */
--gray-100: var(--color-gray-50);
--gray-200: var(--color-gray-100);
--gray-300: var(--color-gray-200);
--gray-400: var(--color-gray-300);
--gray-500: var(--color-gray-400);
--gray-600: var(--color-gray-500);
--gray-700: var(--color-gray-600);
--gray-800: var(--color-gray-700);
--gray-900: var(--color-gray-700);
/* Semantic 별칭 */
--surface: #ffffff;                 /* 원본 순백 유지 (color-surface는 #fafafa) */
--success: #1a7a45;                 /* Design System 미정의 — 원본 유지 */
--warning: #b8690a;                 /* Design System 미정의 — 원본 유지 */
--navy:    #071b44;                 /* Design System 미정의 — 원본 유지 */
--accent:    #f2eb80;
--accent-dk: #c8c040;
--accent-lt: #fdfbe6;
--bg:      #ffffff;
--border:  #ebebeb;
/* Layout */
--sidebar-w:  0px;
--header-h:   68px;
--font:        'SUIT', system-ui, 'Apple SD Gothic Neo', 'Noto Sans KR', -apple-system, sans-serif;
--radius-card: var(--radius-lg);
--radius-btn:  var(--radius-md);
--shadow-card: var(--shadow-m);
/* Legacy spacing aliases — 신규 스타일은 DESIGN.md 공식 spacing만 사용 */
/* Grid */
--grid-gutter: calc(100vw * 3 / 16);
```
