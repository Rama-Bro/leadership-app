import streamlit as st
import time

# --- 설정 ---
TOTAL_TIME = 10 * 60  # 제한 시간 10분 (초 단위)
QUESTIONS = [
    # 자기 인식
    "나는 내 감정 변화를 인식하고 조절하려 노력한다.",
    "내 행동이 타인에게 미치는 영향을 고려한다.",
    "나는 나의 강점과 약점을 비교적 잘 알고 있다.",
    "타인의 피드백을 수용적으로 받아들이는 편이다.",
    # 관계 리더십
    "나는 구성원들과의 신뢰 관계 형성을 중요하게 생각한다.",
    "나는 타인의 입장을 이해하고 공감하려 노력한다.",
    "동료나 부하직원의 의견을 존중하려 노력한다.",
    "관계에서 발생한 갈등을 적극적으로 조율하고 해결하려 한다.",
    # 변화 대응력
    "변화가 생겼을 때 빠르게 적응하는 편이다.",
    "새로운 업무나 환경에 대한 두려움보다 호기심이 더 큰 편이다.",
    "예상치 못한 문제가 발생해도 침착하게 대응하려 노력한다.",
    "새로운 방식이나 시도를 받아들이는 데 유연한 편이다.",
    # 전략적 사고
    "문제를 장기적인 관점에서 바라보려 노력한다.",
    "전체 맥락 속에서 중요한 요인을 찾아내려 한다.",
    "목표 달성을 위한 다양한 대안을 고민한다.",
    "당장의 해결보다 근본 원인을 분석하는 데 집중하는 편이다.",
    # 실행력
    "결정한 일을 실행에 옮기는 데 주저하지 않는다.",
    "업무 계획을 세운 뒤 일정에 맞춰 실천하려 한다.",
    "장기적인 업무도 꾸준히 추진할 수 있다.",
    "마감 기한을 잘 지키는 편이다.",
    # 영향력
    "다른 사람에게 긍정적인 영향을 주려고 노력한다.",
    "내 생각이나 방향을 효과적으로 전달할 수 있다.",
    "상대의 입장을 고려하여 설득 방식을 조율한다.",
    "팀원이나 동료를 격려하고 동기를 부여하려 한다.",
    # 팀 운영 및 육성
    "후배나 동료의 성장을 위해 적극적으로 지원하려 한다.",
    "팀원 각자의 강점을 파악하고 역할을 조율한다.",
    "팀의 성과와 분위기를 균형 있게 고려하려 한다.",
    "성과 창출을 위해 팀원들과 협력하며 일하려 한다."
]

# --- 세션 초기화 ---
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "page" not in st.session_state:
    st.session_state.page = "survey"
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# --- 시간 계산 ---
elapsed = int(time.time() - st.session_state.start_time)
remaining = TOTAL_TIME - elapsed

# --- 상단 고정 타이머 표시 ---
st.markdown(
    f"""
    <div style="position:fixed; top:0; width:100%; background:#fff3cd; padding:10px 0;
                text-align:center; font-size:18px; z-index:999; border-bottom:1px solid #999;">
        ⏳ 남은 시간: <strong>{remaining//60:02d}:{remaining%60:02d}</strong>
    </div>
    <br><br><br>
    """,
    unsafe_allow_html=True
)

# --- 시간 초과시 자동 제출 ---
if remaining <= 0 and not st.session_state.submitted:
    st.session_state.page = "result"
    st.session_state.submitted = True

# --- 설문 화면 ---
if st.session_state.page == "survey":
    st.title("문항 응답")
    st.markdown("문항을 읽고 동의하는 정도에 따라 응답을 선택해주세요.")
    st.caption("1 = 동의하지 않는다 / 5 = 동의한다")

    for i, q in enumerate(QUESTIONS, 1):
        st.radio(
            label=f"{i}. {q}",
            options=[1, 2, 3, 4, 5],
            key=f"q{i}",
            horizontal=True,
            format_func=lambda x: str(x)
        )

    if st.button("제출"):
        st.session_state.page = "result"
        st.session_state.submitted = True

# --- 결과 화면 ---
if st.session_state.page == "result":
    st.title("진단 결과 요약")
    st.success("결과가 성공적으로 제출되었습니다.")
    for i, q in enumerate(QUESTIONS, 1):
        score = st.session_state.get(f"q{i}", "미응답")
        st.write(f"{i}. {q} → 응답: {score}")
