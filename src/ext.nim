import nimpy
import osproc


# Clear progress bars on data load
proc clear(x: string): string {.exportpy.} =
    let clear_output = execCmd(x)
    discard clear_output


# Text Styles
proc red_text(text: string): string {.exportpy.} =
  return "[red]" & text


proc green_text(text: string): string {.exportpy.} =
  return "[green]" & text


proc purple_text(text: string): string {.exportpy.} =
  return "[purple]" & text


proc cyan_text(text: string): string {.exportpy.} =
  return "[cyan]" & text


proc bold_text(text: string): string {.exportpy.} =
  return "[bold]" & text
