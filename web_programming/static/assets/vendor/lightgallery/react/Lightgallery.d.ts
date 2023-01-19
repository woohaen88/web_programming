import * as React from 'react';
import {LightGallerySettings} from '../lg-settings';
import {
    AfterAppendSubHtmlDetail,
    AfterCloseDetail,
    AfterOpenDetail,
    AfterSlideDetail,
    BeforeCloseDetail,
    BeforeNextSlideDetail,
    BeforeOpenDetail,
    BeforePrevSlideDetail,
    BeforeSlideDetail,
    ContainerResizeDetail,
    DragEndDetail,
    DragMoveDetail,
    DragStartDetail,
    FlipHorizontalDetail,
    FlipVerticalDetail,
    InitDetail,
    PosterClickDetail,
    RotateLeftDetail,
    RotateRightDetail,
    SlideItemLoadDetail
} from '../lg-events';

interface LgEvents {
    onAfterAppendSlide?: (detail: AfterSlideDetail) => void;
    onInit?: (detail: InitDetail) => void;
    onHasVideo?: (detail: InitDetail) => void;
    onContainerResize?: (detail: ContainerResizeDetail) => void;
    onAfterAppendSubHtml?: (detail: AfterAppendSubHtmlDetail) => void;
    onBeforeOpen?: (detail: BeforeOpenDetail) => void;
    onAfterOpen?: (detail: AfterOpenDetail) => void;
    onSlideItemLoad?: (detail: SlideItemLoadDetail) => void;
    onBeforeSlide?: (detail: BeforeSlideDetail) => void;
    onAfterSlide?: (detail: AfterSlideDetail) => void;
    onPosterClick?: (detail: PosterClickDetail) => void;
    onDragStart?: (detail: DragStartDetail) => void;
    onDragMove?: (detail: DragMoveDetail) => void;
    onDragEnd?: (detail: DragEndDetail) => void;
    onBeforeNextSlide?: (detail: BeforeNextSlideDetail) => void;
    onBeforePrevSlide?: (detail: BeforePrevSlideDetail) => void;
    onBeforeClose?: (detail: BeforeCloseDetail) => void;
    onAfterClose?: (detail: AfterCloseDetail) => void;
    onRotateLeft?: (detail: RotateLeftDetail) => void;
    onRotateRight?: (detail: RotateRightDetail) => void;
    onFlipHorizontal?: (detail: FlipHorizontalDetail) => void;
    onFlipVertical?: (detail: FlipVerticalDetail) => void;
}

export interface LightGalleryProps extends LgEvents, LightGallerySettings {
    children?: any;
    elementClassNames?: string;
}

declare const LG: React.FC<LightGalleryProps>;
export default LG;
