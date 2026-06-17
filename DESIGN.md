# DESIGN.md — USE 디자인 시스템

> AI(Claude)가 UI 작업 시 참조하는 디자인 관련 내용 전부입니다.
> 작업 규칙·프로세스는 `CLAUDE.md`를 참조하세요.

⚠️ **모든 UI 작업은 아래 디자인 시스템을 기반으로 합니다. 예외 없음.**

---

## 토큰 파일 구조 (3파일 동기화 필수)

| 파일 | 역할 | 수정 기준 |
|------|------|-----------|
| `theme.css` | CSS 변수 정의 — 원본 헥스값은 **여기에만** 존재 | Figma 변수 변경 시에만 |
| `theme.js` | JS 컴포넌트에서 토큰 참조 (JS 객체로 내보내기) | theme.css와 동기화 |
| `tailwind.config.js` | Tailwind 유틸리티 ↔ CSS 변수 매핑 | 토큰 추가/삭제 시에만 |

토큰 추가·수정 시 위 3파일을 **반드시 동시에** 수정합니다.

---

## 색상 토큰

### Gray

| JS 토큰 | CSS 변수 | 값 |
|---------|----------|----|
| `colors.gray[50]` | `--color-gray-50` | #f7f9fc |
| `colors.gray[100]` | `--color-gray-100` | #dce3ec |
| `colors.gray[200]` | `--color-gray-200` | #c4cdd9 |
| `colors.gray[300]` | `--color-gray-300` | #98a2b3 |
| `colors.gray[400]` | `--color-gray-400` | #667085 |
| `colors.gray[500]` | `--color-gray-500` | #475467 |
| `colors.gray[600]` | `--color-gray-600` | #344054 |
| `colors.gray[700]` | `--color-gray-700` | #1d2939 |

### Blue (Brand Primary)

| JS 토큰 | CSS 변수 | 값 |
|---------|----------|----|
| `colors.blue[50]` | `--color-blue-50` | #e7f0ff |
| `colors.blue[100]` | `--color-blue-100` | #dce8ff |
| `colors.blue[200]` | `--color-blue-200` | #c2d9ff |
| `colors.blue[300]` | `--color-blue-300` | #9ec3ff |
| `colors.blue[400]` | `--color-blue-400` | #6fa6ff |
| `colors.blue[500]` | `--color-blue-500` | #126dfb |
| `colors.blue[600]` | `--color-blue-600` | #0f5fe0 |
| `colors.blue[700]` | `--color-blue-700` | #0c4fc2 |
| `colors.blue[800]` | `--color-blue-800` | #093fa3 |
| `colors.blue[900]` | `--color-blue-900` | #003486 |

### Blue Secondary (Material)

| JS 토큰 | CSS 변수 | 값 |
|---------|----------|----|
| `colors.blueSecondary[50]` | `--color-blue-secondary-50` | #e3f2fd |
| `colors.blueSecondary[100]` | `--color-blue-secondary-100` | #bbdefb |
| `colors.blueSecondary[200]` | `--color-blue-secondary-200` | #90caf9 |
| `colors.blueSecondary[300]` | `--color-blue-secondary-300` | #64b5f6 |
| `colors.blueSecondary[400]` | `--color-blue-secondary-400` | #2196f3 |
| `colors.blueSecondary[500]` | `--color-blue-secondary-500` | #1e88e5 |
| `colors.blueSecondary[600]` | `--color-blue-secondary-600` | #1976d2 |
| `colors.blueSecondary[700]` | `--color-blue-secondary-700` | #1565c0 |

### Amber (Warning)

| JS 토큰 | CSS 변수 | 값 |
|---------|----------|----|
| `colors.amber[50]` | `--color-amber-50` | #fff8e1 |
| `colors.amber[100]` | `--color-amber-100` | #ffecb3 |
| `colors.amber[200]` | `--color-amber-200` | #ffe082 |
| `colors.amber[300]` | `--color-amber-300` | #ffd54f |
| `colors.amber[400]` | `--color-amber-400` | #ffc107 |
| `colors.amber[500]` | `--color-amber-500` | #ffb300 |
| `colors.amber[600]` | `--color-amber-600` | #ffa000 |
| `colors.amber[700]` | `--color-amber-700` | #ff8f00 |
| `colors.amber[800]` | `--color-amber-800` | #ff6f00 |

### Red (Error)

| JS 토큰 | CSS 변수 | 값 |
|---------|----------|----|
| `colors.red[50]` | `--color-red-50` | #fdecea |
| `colors.red[100]` | `--color-red-100` | #f9c1bc |
| `colors.red[200]` | `--color-red-200` | #f28b82 |
| `colors.red[300]` | `--color-red-300` | #e57373 |
| `colors.red[400]` | `--color-red-400` | #f44336 |
| `colors.red[500]` | `--color-red-500` | #e53935 |
| `colors.red[600]` | `--color-red-600` | #d32f2f |
| `colors.red[700]` | `--color-red-700` | #c62828 |
| `colors.red[800]` | `--color-red-800` | #b71c1c |

### Semantic

| JS 토큰 | CSS 변수 | 값 | 용도 |
|---------|----------|----|------|
| `colors.semantic.surface` | `--color-surface` | #fafafa | 페이지/카드 기본 배경 |
| `colors.semantic.primary` | `--color-primary` | #1041a7 | 주 브랜드 컬러 |
| `colors.semantic.primaryVariant` | `--color-primary-variant` | #0f5fe0 | 호버/강조 |
| `colors.semantic.onPrimary` | `--color-on-primary` | #ffffff | 주 브랜드 위 텍스트 |
| `colors.semantic.primaryContainer` | `--color-primary-container` | #dce8ff | 연한 브랜드 배경 |
| `colors.semantic.onPrimaryContainer` | `--color-on-primary-container` | #003486 | primaryContainer 위 텍스트 |
| `colors.semantic.shadow` | — | #121212 | 그림자 기준색 |

**올바른 사용 vs 금지:**
```jsx
// ❌ 금지: 헥스 코드 직접 사용
<div style={{ color: '#1d2939', backgroundColor: '#dce3ec' }}>

// ✅ 올바른: theme.js 토큰 참조
import { colors } from './theme.js';
<div style={{ color: colors.gray[700], backgroundColor: colors.gray[100] }}>

// ✅ 올바른: CSS 변수 직접 참조
<div style={{ color: 'var(--color-gray-700)', backgroundColor: 'var(--color-gray-100)' }}>
```

---

## 타이포그래피

**폰트**: SUIT (`typography.fontFamily.base` = `'SUIT', sans-serif`)
`theme.css`에서 CDN으로 로드하거나 프로젝트 내 설치 필요.

### Font Size (8단계)

| JS 토큰 | CSS 변수 | 값 | 용도 |
|---------|----------|----|------|
| `typography.fontSize.displayLg` | `--font-size-display-lg` | 3rem (48px) | 대형 디스플레이 제목 |
| `typography.fontSize.displayMd` | `--font-size-display-md` | 2.5rem (40px) | 중형 디스플레이 제목 |
| `typography.fontSize.displaySm` | `--font-size-display-sm` | 2rem (32px) | 소형 디스플레이 제목 |
| `typography.fontSize.headlineLg` | `--font-size-headline-lg` | 1.75rem (28px) | 대형 헤드라인 |
| `typography.fontSize.headlineMd` | `--font-size-headline-md` | 1.5rem (24px) | 할인율, 중형 헤드라인 |
| `typography.fontSize.headlineSm` | `--font-size-headline-sm` | 1.25rem (20px) | 소형 헤드라인, 섹션 제목 |
| `typography.fontSize.body` | `--font-size-body` | 1rem (16px) | 본문 텍스트, 버튼 라벨 |
| `typography.fontSize.caption` | `--font-size-caption` | 0.75rem (12px) | 캡션, 뱃지, 보조 텍스트 |

### Font Weight (6단계)

| JS 토큰 | CSS 변수 | 값 |
|---------|----------|----|
| `typography.fontWeight.heavy` | `--font-weight-heavy` | 900 |
| `typography.fontWeight.extraBold` | `--font-weight-extra-bold` | 800 |
| `typography.fontWeight.bold` | `--font-weight-bold` | 700 |
| `typography.fontWeight.semiBold` | `--font-weight-semi-bold` | 600 |
| `typography.fontWeight.medium` | `--font-weight-medium` | 500 |
| `typography.fontWeight.regular` | `--font-weight-regular` | 400 |

**올바른 사용 vs 금지:**
```jsx
// ❌ 금지: 토큰에 없는 임의 폰트 사이즈
<p style={{ fontSize: '15px' }}>
<p style={{ fontSize: '18px' }}>

// ✅ 올바른
import { typography } from './theme.js';
<h1 style={{
  fontFamily: typography.fontFamily.base,
  fontSize: typography.fontSize.headlineMd,
  fontWeight: typography.fontWeight.bold,
}}>
  할인율 30%
</h1>
<p style={{
  fontFamily: typography.fontFamily.base,
  fontSize: typography.fontSize.body,
  fontWeight: typography.fontWeight.regular,
  color: colors.gray[500],
}}>
  본문 텍스트
</p>
```

---

## 스페이싱

이 목록 외의 값 사용 금지.

| JS 토큰 | CSS 변수 | 값 | 주요 용도 |
|---------|----------|----|-----------|
| `spacing[2]` | `--spacing-2` | 0.125rem (2px) | 미세 간격 |
| `spacing[4]` | `--spacing-4` | 0.25rem (4px) | 아이콘-텍스트 간격 |
| `spacing[6]` | `--spacing-6` | 0.375rem (6px) | 버튼 내 아이콘 gap |
| `spacing[10]` | `--spacing-10` | 0.625rem (10px) | 뱃지 좌우 패딩 |
| `spacing[12]` | `--spacing-12` | 0.75rem (12px) | 카드 기본 패딩 |
| `spacing[14]` | `--spacing-14` | 0.875rem (14px) | 중간 패딩 |
| `spacing[16]` | `--spacing-16` | 1rem (16px) | 카드 패딩, 버튼 가로 패딩 |
| `spacing[20]` | `--spacing-20` | 1.25rem (20px) | 메인 버튼 가로 패딩 |
| `spacing[32]` | `--spacing-32` | 2rem (32px) | 섹션 간격 |
| `spacing[80]` | `--spacing-80` | 5rem (80px) | 페이지 레벨 여백 |
| `spacing[260]` | `--spacing-260` | 16.25rem (260px) | 고정 레이아웃 너비 |
| `spacing[1000]` | `--spacing-1000` | 62.5rem (1000px) | 최대 너비 컨테이너 |

```jsx
// ❌ 금지: 토큰에 없는 spacing
<div style={{ padding: '8px' }}>
<div style={{ gap: '24px' }}>

// ✅ 올바른
import { spacing } from './theme.js';
<div style={{ padding: spacing[16], gap: spacing[12] }}>
```

---

## Border Radius

| JS 토큰 | CSS 변수 | 값 | 용도 |
|---------|----------|----|------|
| `radius.sm` | `--radius-sm` | 0.25rem (4px) | 소형 요소 |
| `radius.md` | `--radius-md` | 0.75rem (12px) | 버튼, 입력 필드 |
| `radius.lg` | `--radius-lg` | 1rem (16px) | 카드 (CouponCard) |
| `radius.full` | `--radius-full` | 9999px | Pill 형태 (뱃지) |

---

## Shadow

| JS 토큰 | CSS 변수 | 값 | 용도 |
|---------|----------|----|------|
| `shadow.s` | `--shadow-s` | 0px 2px 15px 2px rgba(18,18,18,0.05) | 미묘한 그림자 |
| `shadow.m` | `--shadow-m` | 0px 3px 13px -3px rgba(18,18,18,0.20) | 카드 기본 그림자 |
| `shadow.l` | `--shadow-l` | 0px 5px 10px -3px rgba(18,18,18,0.20) | 강조 그림자 |

---

## 컴포넌트 사용 가이드

모든 컴포넌트는 `components/` 하위에 위치합니다.

```jsx
import Button     from './components/Button/Button.jsx';
import Badge      from './components/Badge/Badge.jsx';
import CouponCard from './components/CouponCard/CouponCard.jsx';
```

### Button

```
variant   : 'primary' | 'secondary' | 'tertiary'
size      : 'detail' (52px) | 'main' (60px)
상태      : disabled / loading
icon      : ReactNode — iconPosition 'left' | 'right'
fullWidth : boolean
```

```jsx
<Button label="확인"      variant="primary"   size="detail" />
<Button label="확인"      variant="primary"   size="main" />
<Button label="취소"      variant="secondary" />
<Button label="더보기"    variant="tertiary" />
<Button label="전송"      variant="primary"   disabled />
<Button label="처리중"    variant="primary"   loading />
<Button label="검색"      variant="primary"   icon={<SearchIcon />} iconPosition="left" />
<Button label="다음"      variant="primary"   icon={<ArrowIcon />}  iconPosition="right" />
<Button label="전체 너비" variant="primary"   fullWidth />
```

### Badge

```
type : 'dday' | 'dday-soft' | 'dn' | 'dn-soft'
     | 'price' | 'usage' | 'distance' | 'channel' | 'number'
```

```jsx
<Badge type="dday"      label="D-3" />
<Badge type="dday-soft" label="D-3" />
<Badge type="dn"        label="D+5" />
<Badge type="dn-soft"   label="D+5" />
<Badge type="price"     label="5,000원" />
<Badge type="distance"  label="500m" icon={<PinIcon />} />
<Badge type="channel"   label="온라인" />

// usage: usageState = 'available' | 'used' | 'expired'
<Badge type="usage" usageState="available" label="사용 가능" />
<Badge type="usage" usageState="used"      label="사용 완료" />
<Badge type="usage" usageState="expired"   label="기간 만료" />

// number: numberVariant = 'default' | 'soft' | 'inactive' | 'small' | 'outlined'
<Badge type="number" count={9} numberVariant="default" />
<Badge type="number" count={9} numberVariant="soft" />

// pressed 상태
<Badge type="dday" label="D-3" pressed />
```

### CouponCard

```
layout : 'vertical' | 'vertical-wide' | 'vertical-ext'
       | 'horizontal-sm' | 'horizontal-md' | 'horizontal-lg' | 'horizontal-xl'
```

```jsx
// 세로형 (152×200)
<CouponCard layout="vertical"      discount="30%"      label="전 상품 할인" expiryLabel="~2025.12.31" />

// 세로형 쿠폰 (159×276)
<CouponCard layout="vertical-wide" discount="5,000원"  label="할인 쿠폰" description="최소 30,000원 이상" expiryLabel="~2025.12.31" />

// 세로형 확장 — 기본 배경 amber[800], 흰 텍스트 (160×220)
<CouponCard layout="vertical-ext"  discount="20%"      label="앱 전용" expiryLabel="~2025.12.31" />

// 가로형 (362×96~228)
<CouponCard layout="horizontal-sm" discount="10%"      label="소형 쿠폰" />
<CouponCard layout="horizontal-md" discount="15%"      label="중형 쿠폰" description="전 상품 적용" />
<CouponCard layout="horizontal-lg" discount="30%"      label="대형 쿠폰" />   // 기본 배경 blue[700]
<CouponCard layout="horizontal-xl" discount="50,000원" label="특대형 쿠폰" description="10만원 이상 구매 시" />

// 비활성화
<CouponCard layout="vertical" discount="30%" label="만료 쿠폰" disabled />

// 커스텀 배경색 — theme.js 변수만 허용
<CouponCard layout="vertical" accentColor={colors.blue[500]} discount="20%" label="특가" />

// 클릭 가능
<CouponCard layout="horizontal-md" discount="15%" label="쿠폰" onClick={() => handleSelect()} />
```

---

## ⛔ 디자인 시스템 금지사항

| # | 금지 | 올바른 방법 | 예시 |
|---|------|-------------|------|
| 1 | 헥스 코드 직접 사용 | JS 토큰 또는 CSS 변수 사용 | `'#126dfb'` → `colors.blue[500]` |
| 2 | 토큰에 없는 color 사용 | 팔레트 내 nearest 값 사용 | `'#aabbcc'` → `colors.gray[200]` 등 |
| 3 | 토큰에 없는 spacing | 정의된 spacing 키만 사용 | `'8px'` → `spacing[10]` 또는 `spacing[6]` |
| 4 | 토큰에 없는 font-size | 8단계 scale만 사용 | `'15px'` → `typography.fontSize.body` |
| 5 | rgba() 하드코딩 | shadow 토큰 사용 | `rgba(0,0,0,0.1)` → `shadow.s` |
| 6 | 기존 컴포넌트 중복 생성 | `components/` 재사용 | 새 버튼 → `<Button variant="...">` |
| 7 | 컴포넌트 내부 스타일 직접 수정 | props로 제어 | `.Button { background: red }` → `accentColor` prop |
| 8 | 토큰 1~2파일만 수정 | 3파일 동시 수정 | theme.css만 → theme.css + theme.js + tailwind.config.js |

---

## 새 토큰 추가 절차

> 예: `colors.green[500]` (#22C55E) 추가가 필요한 경우

**1단계: Figma 변수 확인 후 사용자 승인 요청**

**2단계: 승인 후 3파일 동시 수정**

```css
/* theme.css */
:root {
  --color-green-500: #22C55E;
}
```

```js
// theme.js
export const colors = {
  green: { 500: '#22C55E' },
};
```

```js
// tailwind.config.js
colors: {
  green: { 500: 'var(--color-green-500)' },
},
```

**3단계: 사용**
```jsx
import { colors } from './theme.js';
<span style={{ color: colors.green[500] }}>완료</span>
```
