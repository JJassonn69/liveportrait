# coding: utf-8
from liveportrait.core.config.argument_config import ArgumentConfig
from liveportrait.core.config.inference_config import InferenceConfig
from liveportrait.core.config.crop_config import CropConfig
from liveportrait.core.live_portrait_pipeline import LivePortraitPipeline

class Inference:
    def __init__(self, source_image=None, driving_info=None):
        self.args = ArgumentConfig()
        self.args.source_image = source_image
        self.args.driving_info = driving_info

    def _partial_fields(self, target_class, kwargs):
        """Partial initialization of target_class fields with kwargs"""
        return target_class(**{k: v for k, v in kwargs.items() if hasattr(target_class, k)})

    def _run_inference(self):
        """Run the live portrait inference pipeline"""
        # Specify configs for inference
        inference_cfg = self._partial_fields(InferenceConfig, self.args.__dict__)
        crop_cfg = self._partial_fields(CropConfig, self.args.__dict__)

        # Initialize the live portrait pipeline
        live_portrait_pipeline = LivePortraitPipeline(
            inference_cfg=inference_cfg,
            crop_cfg=crop_cfg
        )

        # Run the pipeline
        return live_portrait_pipeline.execute(self.args)

    def run(self, source_image=None, driving_video=None):
        """
        Run the live portrait inference.

        Args:
            source_image (str): Path to the source image.
            driving_video (str): Path to the driving video or animation.

        Returns:
            The result of the live portrait inference pipeline.
        """
        if source_image is not None:
            self.args.source_image = source_image
        if driving_video is not None:
            self.args.driving_info = driving_video

        return self._run_inference()
