# manim -pqh .\manim\demo\main.py Demo

from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

from manim import *

# from manim_voiceover.services.elevenlabs import ElevenLabsService


class Demo(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", transcription_model="base"))
        # self.set_speech_service(ElevenLabsService(
        # voice_id="sJGczbJuIrCAxW19pP8P",
        # ))

        circle = Circle()

        with self.voiceover(
            text="This circle is drawn as I speak. The scene will wait for this sentence to finish before proceeding."
        ):
            self.play(Create(circle))

        with self.voiceover(
            text="Let's shift the circle to the left 2 units... This animation takes as long as this text to be read."
        ) as tracker:
            self.play(circle.animate.shift(2 * LEFT), run_time=tracker.duration)

        self.play(Uncreate(circle))

        blist = BulletedList(
            "Trigger animations", "At any word", "Bookmarks", font_size=64
        )

        with self.voiceover(
            text="""You can <bookmark mark='A'/>trigger animations <bookmark mark='B'/>at any word in the middle of a sentence by adding <bookmark mark='C'/>bookmarks to your text."""
        ) as tracker:
            self.wait_until_bookmark("A")

            self.play(
                Write(blist[0]), run_time=tracker.time_until_bookmark("B", limit=1)
            )
            self.wait_until_bookmark("B")
            self.play(
                Write(blist[1]), run_time=tracker.time_until_bookmark("C", limit=1)
            )
            self.wait_until_bookmark("C")
            self.play(Write(blist[2]))

        self.play(FadeOut(blist))

        s32s_text = Tex("Supercalifragilisticexpialidocious", font_size=72)
        super_text = s32s_text[0][:5]
        cali_text = s32s_text[0][5:9]
        fragilistic_text = s32s_text[0][9:20]
        expiali_text = s32s_text[0][20:27]
        docious_text = s32s_text[0][27:]

        with self.voiceover(
            text="Here is another example for more fine-tuned bookmarking. Super<bookmark mark='A'/>cali<bookmark mark='B'/>fragilistic<bookmark mark='C'/>expiali<bookmark mark='D'/>docious."
        ) as tracker:
            self.play(
                super_text.animate.set_color(RED),
                run_time=tracker.time_until_bookmark("A"),
            )
            self.play(
                cali_text.animate.set_color(ORANGE),
                run_time=tracker.time_until_bookmark("B"),
            )
            self.play(
                fragilistic_text.animate.set_color(YELLOW),
                run_time=tracker.time_until_bookmark("C"),
            )
            self.play(
                expiali_text.animate.set_color(GREEN),
                run_time=tracker.time_until_bookmark("D"),
            )
            self.play(
                docious_text.animate.set_color(BLUE),
                run_time=tracker.get_remaining_duration(),
            )

        self.play(FadeOut(s32s_text))
        square = Square()

        with self.voiceover(
            text="""Now let's talk about subtitles. Subtitles are automatically generated as a ".srt" file next to the video output. By default, the subtitle is the same as the text, however you can modify this behavior by specifying the subcaption property.""",
            subcaption="This is a custom subcaption that lasts the duration of this scene. You can say other things instead of the caption.",
        ) as tracker:
            self.play(Create(square), run_time=tracker.duration)

        with self.voiceover(
            text="""Why would this be helpful? Many times, we want to insert LaTeX into the subcaptions, however the text-to-speech isn't able to pronounce it correctly. As an example, here's the L2 norm of a vector and Mass-energy Equivalence.""",
            subcaption=r"""Why would this be helpful? Many times, we want to insert LaTeX into the subcaptions, however the text-to-speech isn't able to pronounce it correctly. As an example, here's $\left\lVert{x}\right\rVert_2$ and $e = mc^2$""",
        ) as tracker:
            self.play(Uncreate(square), run_time=tracker.duration)

        with self.voiceover(
            text="""This also allows us to add SSML-like customizations to the voiceover, like "insert emotion" into the voices ———————— or add "pauses"....... without affecting the subcaption. This works on ElevenLabs... but not GTTS.""",
            subcaption="""This also allows us to add SSML-like customizations to the voiceover, like insert emotion into the voices, or add pauses... without affecting the subcaption. This works on ElevenLabs but not GTTS.""",
        ) as tracker:
            self.play(Create(circle), run_time=tracker.duration)

        self.wait()
